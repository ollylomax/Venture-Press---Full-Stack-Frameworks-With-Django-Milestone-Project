from django.db import models

from accounts.models import UserProfile
from checkout.models import Order


def artwork_directory(instance, filename):
    """
    Function to set custom save directory destination and naming format to
    files passed in as arguments.
    """
    return 'artwork/order_{0}/{1}'.format(instance.order, filename)


class Artwork(models.Model):
    """
    Artwork class model with two foreign key fields from UserProfile and Order
    models, and an upload file field which passes uploaded files to the artwork
    directory function.
    """

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    upload = models.FileField(upload_to=artwork_directory)
