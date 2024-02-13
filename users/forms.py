from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import TextInput

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('phone_number',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'phone_number')


class CustomUserChangeInf(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('surname', 'name', 'middlename', 'email', 'phone_number', 'avatar', 'nickname')
        widgets = {
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "middlename": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            "phone_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
            "nickname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Псевдоним'
            }),


        }


