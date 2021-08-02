from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.AllPassword.as_view(), name='home'),
    path('edit-password/<pk>', views.EditAccount.as_view(), name='edit-password'),
    path('delete/<pk>', views.DeleteAccount.as_view(), name='delete-password'),


    path('register', views.RegisterPage.as_view(), name='register'),
    path('login', views.CustomLogin.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),

    path('add-mail', views.AddMail.as_view(), name='add-mail'),
    path('all-mail', views.AllEmail.as_view(), name='all-mail'),
    path('all-mail/<pk>', views.DeleteMail.as_view(), name='delete-mail'),
    path('edit-mail/<pk>', views.EditMail.as_view(), name='edit-mail'),

    path('add-phone', views.AddPhone.as_view(), name='add-phone'),
    path('all-phone', views.AllPhone.as_view(), name='all-phone'),
    path('all-phone/<pk>', views.DeletePhone.as_view(), name='delete-phone'),
    path('edit-phone/<pk>', views.EditPhone.as_view(), name='edit-phone'),

    path('add-password', views.AddPassword.as_view(), name='add-password')
]
