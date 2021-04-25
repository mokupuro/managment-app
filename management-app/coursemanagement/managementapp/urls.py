from django.urls import path
from .views import Login, Logout, UserCreate, UserCreateComplete, UserCreateDone, UserDetail, UserUpdate
from .views import SyllabusListView, listfunc 

urlpatterns = [

    path('login/', Login.as_view(), name='login'),
    path('logout/',Logout.as_view(), name='logout'),
    path('user_create/', UserCreate.as_view(), name='user_create'),
    path('user_create/done/', UserCreateDone.as_view(), name='user_create_done'),
    path('user_create/complete/<token>/', UserCreateComplete.as_view(), name='user_create_complete'),

    # ユーザーページ情報
    path('user_detail/<int:pk>/', UserDetail.as_view(), name='user_detail'),
    path('user_update/<int:pk>/', UserUpdate.as_view(), name='user_update'),

    # 一覧画面
    path('', SyllabusListView.as_view(), name='index'),
    
    path('list/', listfunc, name='list')
]