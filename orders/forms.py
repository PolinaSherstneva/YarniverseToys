from django import forms
from django.forms import TextInput, Select

from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['city', 'street',  'house', 'apartment']


class OrderChangeStatus(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']

        widgets = {
            "status": Select(attrs={
                'select': 'Статус'
            }),
        }
