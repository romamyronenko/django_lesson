from django.contrib.auth.models import User
from django.http import HttpResponse
from django.test import TestCase, RequestFactory
from django.urls import reverse, resolve

from main.views import index


# Create your tests here.
class ToDoListTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="TestUser", email='', password='pass'
        )

    def test_index(self):
        request = self.factory.get("/")
        request.user = self.user
        response: HttpResponse = index(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f"<h1>{self.user.username}</h1>")

    def test_url(self):
        url = reverse('main:home')

        self.assertEqual(resolve(url).func, index)
        self.assertEqual(url, "/")
