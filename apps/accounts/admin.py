from django.contrib import admin
from apps.base_accounts.admin import EmailUserAdmin
from .models import EmailUser


class UserAdmin(EmailUserAdmin):
    pass
admin.site.register(EmailUser, EmailUserAdmin)
