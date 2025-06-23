from django.contrib import admin
from boards.models import Board


# Register your models here.
@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    pass