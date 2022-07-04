from django.db import models

from accounts.models import UserProfile
from checkout.models import Order


def artwork_directory(instance, filename):
    return 'artwork/order_{0}/{1}'.format(instance.order, filename)


class Artwork(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    upload = models.FileField(upload_to=artwork_directory)