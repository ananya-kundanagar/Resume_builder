# file: todo_project/login_app/admin.py

from django.contrib import admin
from .models import PasswordResetRequest


admin.site.register(PasswordResetRequest)