from django.db import models
from django.contrib.auth.models import User


SUBJECTS = (
    ('GENERAL', 'General'),
    ('QUOTE', 'Quote'),
    ('COMPLAINT', 'Complaint'),
    ('PARTNERS', 'Partners'),
)


class Messages(models.Model):
    """
    Contact model for contact and success views
    """
    class Meta:
        verbose_name_plural = 'Messages'

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=15, null=False, blank=False)
    last_name = models.CharField(max_length=15, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    subject = models.CharField(max_length=10, choices=SUBJECTS, default='GENERAL')
    message = models.TextField(max_length=200, null=False, blank=False) 

