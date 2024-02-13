
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['surname', 'name', 'middlename',  'phone_number', 'email']
    list_display_links = ['surname', 'name', 'middlename',  'phone_number', 'email']

    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Пользовательская информация',
            {
                'fields': (
                    'surname',
                    'name',
                    'middlename',
                    'fullname',
                    'phone_number',


                )
            }
        )
    )
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Пользовательская информация',
            {
                'fields': (
                    'surname',
                    'name',
                    'middlename',
                    'fullname',
                    'phone_number',


                )
            }
        )
    )


admin.site.register(CustomUser, CustomUserAdmin)

