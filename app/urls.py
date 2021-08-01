from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.AllPassword.as_view(), name='home'),
    path('register', views.RegisterPage.as_view(), name='register'),
    path('login', views.CustomLogin.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),

    path('add-mail', views.AddMail.as_view(), name='add-mail'),
    path('all-mail', views.AllEmail.as_view(), name='all-mail'),

    path('add-phone', views.AddPhone.as_view(), name='add-phone'),
    path('all-phone', views.AllPhone.as_view(), name='all-phone'),

    path('add-password', views.AddPassword.as_view(), name='add-password')
]
