from django.db import models


class Product(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('passive', 'Passive'),
    ]
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    status = models.CharField(max_length=7, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name
