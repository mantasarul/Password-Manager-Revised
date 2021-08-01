from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Mail, Phone, Account

# Register your models here.

class MailModel(admin.ModelAdmin):
    list_display = ['mail']


class PhoneModel(admin.ModelAdmin):
    list_display = ['phone']


class AccountModel(admin.ModelAdmin):
    list_display = [
        'user',
        'category',
        'url',
        'username',
        'password',
        'mail_id',
        'phone_id',
        'recovery_code',
    ]


admin.site.register(Mail, MailModel)
admin.site.register(Phone, PhoneModel)
admin.site.register(Account, AccountModel)