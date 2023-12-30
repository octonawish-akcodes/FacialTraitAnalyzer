# age_gender_detection_app/urls.py
from django.urls import path
from .views import upload_image

urlpatterns = [
    path('upload/', upload_image, name='upload_image'),
]
