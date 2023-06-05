from django.urls import path
from .views import *

urlpatterns = [
    path('', image_view, name='image_upload'),
]

