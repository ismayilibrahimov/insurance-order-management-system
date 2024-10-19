from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from products.models import Product
from orders.models import Order


User = get_user_model()

class OrderTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user', password='pass')
        self.product = Product.objects.create(
            name='Test Product', price=100, description='Test', status='active'
        )
        response = self.client.post(reverse('login'), {'username': 'user', 'password': 'pass'})
        self.token = response.data['access']


    def test_create_order(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        url = reverse('order-create')
        response = self.client.post(url, {'product': self.product.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    

    def test_get_order_list(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        url = reverse('order-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_order_status(self):
        order = Order.objects.create(user=self.user, product=self.product)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        url = reverse('order-status', kwargs={'pk': order.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'pending')
