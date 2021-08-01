from app.models import Account, Mail, Phone
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

# class Home(TemplateView):
#     template_name = 'home.html'


class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegisterPage, self).get(*args, **kwargs)


class CustomLogin(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    # success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')


class AddMail(LoginRequiredMixin, CreateView):
    template_name = 'add-mail.html'
    model = Mail
    fields = ['mail']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user_mail = self.request.user
        return super(AddMail, self).form_valid(form)    


class AllEmail(LoginRequiredMixin, ListView):
    model = Mail
    context_object_name = 'mails'
    template_name = 'all-mail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mails'] = context['mails'].filter(user_mail=self.request.user)
        return context


class AddPhone(LoginRequiredMixin, CreateView):
    template_name = 'add-phone.html'
    model = Phone
    fields = ['phone']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user_phone = self.request.user
        return super(AddPhone, self).form_valid(form)    


class AllPhone(LoginRequiredMixin, ListView):
    model = Phone
    context_object_name = 'numbers'
    template_name = 'all-phone.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['numbers'] = context['numbers'].filter(user_phone=self.request.user)
        return context


class AddPassword(LoginRequiredMixin, CreateView):
    template_name = 'add-password.html'
    model = Account
    fields = ['category', 'url', 'username', 'password', 'mail_id', 'phone_id', 'recovery_code']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddPassword, self).form_valid(form)   


class AllPassword(LoginRequiredMixin, ListView):
    model = Account
    context_object_name = 'passwords'
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['passwords'] = context['passwords'].filter(user=self.request.user)
        return context