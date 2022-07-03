from django.db import models

from accounts.models import UserProfile
from checkout.models import Order


class Artwork(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    upload = models.FileField(upload_to='artwork/%d/%m/%Y')