from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Service(models.Model):

    PAPER_SIZE_CHOICES = [
        ('A2', 'A2'),
        ('A3', 'A3'),
        ('A4', 'A4'),
        ('A5', 'A5'),
        ('A6', 'A6'),
    ]

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    paper_size = models.CharField(
        max_length=2,
        choices=PAPER_SIZE_CHOICES,
        default='A4',
    )
    

    def __str__(self):
        return self.name