from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


# Register your models here.
@admin.register(User)
class CostomUserAdmin(UserAdmin):
    list_display = ("username", "email", "is_business", "grade",)
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )