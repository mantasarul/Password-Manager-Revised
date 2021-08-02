from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mail(models.Model):
    user_mail = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    mail = models.EmailField(unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.mail}"


class Phone(models.Model):
    user_phone = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.phone}"


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mail_id = models.ForeignKey(Mail, on_delete=models.CASCADE, null=True, blank=True)
    phone_id = models.ForeignKey(Phone, on_delete=models.CASCADE, null=True, blank=True)
    category = models.CharField(max_length=100)
    url = models.CharField(max_length=1000, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=500)
    recovery_code = models.CharField(max_length=1000, null=True, blank=True)    

    def __str__(self):
        return f"{self.user} {self.mail_id} {self.phone_id} {self.category} {self.url} {self.username} {self.password} {self.password} {self.recovery_code}"

