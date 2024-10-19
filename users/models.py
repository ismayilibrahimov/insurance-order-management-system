from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
from django.contrib.contenttypes.models import ContentType
from orders.models import Order
from products.models import Product


class User(AbstractUser):
    ROLE_CHOICES = [
        ('user', 'User'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=5, choices=ROLE_CHOICES, default='user')


    def save(self, *args, **kwargs):
        self.is_staff = self.is_superuser or (self.role == 'admin')
        super().save(*args, **kwargs)
        self.update_permissions()


    def update_permissions(self):
        content_type_order = ContentType.objects.get_for_model(Order)
        content_type_product = ContentType.objects.get_for_model(Product)

        if self.role == 'admin':
            permissions = [
                Permission.objects.get(codename='view_order', content_type=content_type_order),
                Permission.objects.get(codename='change_order', content_type=content_type_order),
                Permission.objects.get(codename='view_product', content_type=content_type_product),
                Permission.objects.get(codename='change_product', content_type=content_type_product),
            ]
            self.user_permissions.set(permissions)
        else:
            self.user_permissions.clear()
