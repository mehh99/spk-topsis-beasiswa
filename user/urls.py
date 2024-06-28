# user/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_main, name='user'),
    path('register/', views.register, name='register'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('<int:user_id>/login-history/', views.user_login_history, name='user_login_history'),
]
