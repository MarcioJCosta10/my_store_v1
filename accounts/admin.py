from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import GuestEmail
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()
admin.site.register(User)
admin.site.register(GuestEmail)
# Register your models here.