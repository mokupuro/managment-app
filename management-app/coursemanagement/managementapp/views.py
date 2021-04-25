from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import BadSignature, SignatureExpired, loads, dumps
from django.contrib.auth import get_user_model, login
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DetailView
from django.views.generic.edit import CreateView
from django.template.loader import render_to_string
from django.shortcuts import redirect, resolve_url

import urllib.request
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys
import chromedriver_binary


from .models import User, Syllabus
from .forms import LoginForm, UserUpdateForm, UserCreateForm


User = get_user_model()
url = "https://www.e-campus.gr.jp/syllabus/kanri/hachioji/public/syllabus/2021"
driver = webdriver.Chrome()


# ログインページ
class Login(LoginView):
    form_class = LoginForm
    template_name = 'login.html'


# ログアウトページ
class Logout(LogoutView):
    template_name = 'base.html'


# 一覧画面
class SyllabusListView(CreateView):
    model = Syllabus
    fields = ('cource', 'others', 'semester', 'lecture_type')
    success_url = reverse_lazy('list')


# シラバスのスクレイピング

def listfunc(request):
    driver.get(url)

    for post in Syllabus.objects.all():
        cource = post.cource
        others = post.others
        semester = post.semester
        lecture_type = post.lecture_type


    list = []

    el_discipline = driver.find_element_by_id("discipline-select")
    el_others_grade = driver.find_element_by_id("q_others_grade_id")
    el_semester = driver.find_element_by_id("q_semester_id_eq")
    el_choice_type = driver.find_element_by_id("q_choice_type_id_eq")

    print(cource, others, semester, lecture_type)
    Select(el_discipline).select_by_value(str(cource))
    Select(el_others_grade).select_by_value(str(others))
    Select(el_semester).select_by_value(str(semester))
    Select(el_choice_type).select_by_value(str(lecture_type))


    el_choice_type.send_keys(keys.ENTER)

    # sleep(5)

    cur_url = driver.current_url
    print(driver.current_url)
    # driver.close()

    # requestsでhtmlをダウンロード
    response = requests.get(cur_url)
    # # BeautifulSoupで解析、取り出し
    bs = BeautifulSoup(response.content, "html.parser")


    curriculums = bs.select("body > div.container > div.row > div.span12 > div.section > div.section-content > div.span6 > div > a")

    for curriculum in curriculums:
        list.append(curriculum.getText())

    context = {'list': list}
    print(context)

    return render(request, 'list.html', context)


# ユーザー仮登録
class UserCreate(CreateView):
    template_name = 'user_create.html'
    form_class = UserCreateForm

    def form_valid(self, form):
        """仮登録と本登録用メールの発行."""
        # 仮登録と本登録の切り替えは、is_active属性を使うと簡単です。
        # 退会処理も、is_activeをFalseにするだけにしておくと捗ります。
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        # アクティベーションURLの送付
        current_site = get_current_site(self.request)
        domain = current_site.domain
        context = {
            'protocol': self.request.scheme,
            'domain': domain,
            'token': dumps(user.pk),
            'user': user,
        }

        subject = render_to_string('mail_template/create/subject.txt', context)
        message = render_to_string('mail_template/create/message.txt', context)

        user.email_user(subject, message)
        return redirect('user_create_done')


# ユーザー仮登録
class UserCreateDone(TemplateView):
    template_name = 'user_create_done.html'


# メール内アクセス後のユーザー本登録
class UserCreateComplete(TemplateView):
    template_name = 'user_create_complete.html'
    timeout_seconds = getattr(settings, 'ACTIVATION_TIMEOUT_SECONDS', 60*60*24)  # デフォルトでは1日以内

    def get(self, request, **kwargs):
        """tokenが正しければ本登録."""
        token = kwargs.get('token')
        try:
            user_pk = loads(token, max_age=self.timeout_seconds)

        # 期限切れ
        except SignatureExpired:
            return HttpResponseBadRequest()

        # tokenが間違っている
        except BadSignature:
            return HttpResponseBadRequest()

        # tokenは問題なし
        else:
            try:
                user = User.objects.get(pk=user_pk)
            except User.DoesNotExist:
                return HttpResponseBadRequest()
            else:
                if not user.is_active:
                    # 問題なければ本登録とする
                    user.is_active = True
                    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    user.save()
                    return super().get(request, **kwargs)

        return HttpResponseBadRequest()


class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        # 今ログインしてるユーザーのpkと、そのユーザー情報ページのpkが同じか、又はスーパーユーザーなら許可
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser

class UserDetail(OnlyYouMixin, DetailView):
    model = User
    template_name = 'user_detail.html'


class UserUpdate(OnlyYouMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'user_form.html'

    def get_success_url(self):
        return resolve_url('user_detail', pk=self.kwargs['pk'])
