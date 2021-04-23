from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .models import User, Syllabus
from .forms import UserForm

# Create your views here.

# 一覧画面
class SyllabusListView(ListView):
    model = Syllabus

# 登録画面
class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('index')