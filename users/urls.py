from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "users"

urlpatterns = [
    path('', views.main, name='main'),
    path("login/", views.login_view.as_view(), name="log_in"),
    path("signup/", views.sign_up, name="sign_up"),
    path("logout/", views.log_out, name="log_out"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)