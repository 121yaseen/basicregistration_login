from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = "registration"
urlpatterns = [
    path('register', Register.as_view(), name='register'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
