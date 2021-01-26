from django.test import TestCase
from django.contrib.auth.models import User


class LoginTest(TestCase):
    def setUp(self):
        self.url = '/user/login/'
        self.user = User.objects.create(username='test@123.com')
        self.user.set_password('test@123')
        self.user.save()

    def test_get_page(self):
        res = self.client.get(self.url)
        self.assertContains(res, "<input")

    def test_for_login(self):
        res = self.client.post(self.url, {
            'username': 'test@123.com',
            'password': 'test@123'
            })
        self.assertRedirects(res, '/user/profile/')


class LogoutTest(TestCase):
    def test_logout(self):
        res = self.client.get('/user/logout/')
        self.assertRedirects(res, '/user/login/')


class RegistrationTest(TestCase):
    def setUp(self):
        self.url = '/user/register/'
        self.data = {
            'username': 'testuser1234',
            'email': 'testuser@123.com',
            'password1': 'abc@12345678',
            'password2': 'abc@12345678',
            }

    def test_get_page(self):
        res = self.client.get(self.url)
        self.assertContains(res, "Registration")

    def test_register(self):
        res = self.client.post(self.url, self.data)
        user = User.objects.get(username=self.data['username'])
        self.assertEqual(user.email, self.data['email'])
        self.assertRedirects(res, '/user/login/')

    def test_register_without_email(self):
        del self.data['email']
        res = self.client.post(self.url, self.data)
        self.assertContains(res, "This field is required")
        

