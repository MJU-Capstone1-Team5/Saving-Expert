from django.contrib import admin
from .models import Board, Boardcategory, Boardcomment

# Register your models here.
@admin.register(Board)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Boardcategory)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Boardcomment)
class PostAdmin(admin.ModelAdmin):
    pass
