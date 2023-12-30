from django.db import models

# age_gender_detection_app/models.py

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
