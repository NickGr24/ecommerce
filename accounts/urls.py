from django.urls import path

from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('register/', views.reg_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('accounts/login/', views.login_page, name='login'),
]
