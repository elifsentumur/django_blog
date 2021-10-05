from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.db.models.expressions import F
from account.models import CustomUserModel

@admin.register(CustomUserModel)
class CustomAdmin(UserAdmin):
    list_display =('username','email')
    fieldsets = UserAdmin.fieldsets + (
        ('Avatar  Değiştirme Alanı', {
           'fields':['avatar'] 
        }),
    )

