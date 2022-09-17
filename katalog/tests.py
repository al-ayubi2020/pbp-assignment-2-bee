from django.test import TestCase, Client
from django.urls import reverse, resolve
from katalog.views import show_catalog

class TestUrls(TestCase):

    def test_template(self):
        client = Client()
        response = client.get(reverse("katalog:show_catalog"))
        url = reverse('katalog:show_catalog')
        self.assertEquals(resolve(url).func, show_catalog)

    def test_urls(self):
        c = Client()
        url = reverse('katalog:show_catalog')
        response = c.get(url)
        self.assertEquals(response.status_code, 200)
