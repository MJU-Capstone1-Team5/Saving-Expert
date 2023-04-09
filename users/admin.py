from django.contrib import admin
from .models import Myuser
# Register your models here.
@admin.register(Myuser)
class PostAdmin(admin.ModelAdmin):
    pass