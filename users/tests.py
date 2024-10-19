from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User


class UserTests(APITestCase):
    def test_user_signup(self):
        url = reverse('signup')
        data = {'username': 'testuser', 'email': 'user@example.com', 'password': 'pass'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.get().username, 'testuser')


    def test_user_login(self):
        User.objects.create_user(username='testuser', email='user@example.com', password='pass')
        url = reverse('login')
        data = {'username': 'testuser', 'password': 'pass'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)


    def test_login_with_invalid_credentials(self):
        url = reverse('login')
        data = {'username': 'nonexistent', 'password': 'wrongpassword'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
