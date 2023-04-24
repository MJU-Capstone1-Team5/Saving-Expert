from django.contrib import admin
from .models import Budgetcategory, Budget

# Register your models here.

@admin.register(Budget)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Budgetcategory)
class PostAdmin(admin.ModelAdmin):
    pass