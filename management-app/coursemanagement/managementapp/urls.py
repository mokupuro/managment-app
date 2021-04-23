from django.urls import path
from .views import SyllabusListView, UserCreateView

urlpatterns = [
    # 一覧画面
    path('',  SyllabusListView.as_view(), name='index'),

    # 登録画面
    path('create/', UserCreateView.as_view(), name='create'),
]