from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    surname = models.CharField(max_length=100, verbose_name="Фамилия")
    name = models.CharField(max_length=100, verbose_name="Имя")
    middlename = models.CharField(max_length=100, verbose_name="Отчество")
    email = models.EmailField(verbose_name='Почтовый адрес')
    nickname = models.CharField(max_length=100, verbose_name="Псевдоним")
    avatar = models.ImageField(upload_to='tovar/%Y/%m/%d', blank=True)
    phone_number = models.CharField(max_length=100, verbose_name="Номер телефона", unique=True )
    # status = models.BooleanField(default=False, verbose_name='Подтверждение аккаунта')#

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.name
