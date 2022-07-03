from django.db import models

class Artwork(models.Model):
    upload = models.FileField(upload_to='artwork/%d/%m/%Y')
