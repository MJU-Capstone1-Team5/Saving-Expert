from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "boards"

urlpatterns = [
    path('', views.board, name='board'),
    path('<int:id>',views.detail, name='detail'),
    path('create',views.create, name='create'),
    path('update/<int:id>',views.update, name='update'),
    path('delete/<int:id>',views.delete, name='delete'),
    path('commentdelete/<int:id>/<int:bid>', views.commentdelete, name='commentdelete'),
    path('commentcreate/<int:id>', views.commentcreate, name='commentcreate'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)