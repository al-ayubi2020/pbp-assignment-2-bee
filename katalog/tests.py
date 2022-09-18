from django.test import TestCase, Client
from django.urls import reverse, resolve
from katalog.views import show_catalog
from katalog.models import CatalogItem

class TestUrls(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('katalog:show_catalog')
        self.response = self.client.get(self.url)

    def test_url(self):
        self.assertEquals(resolve(self.url).func, show_catalog)

    def test_view(self):
        self.assertEquals(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "katalog.html")

    def test_models(self):
        CatalogItem.objects.create(item_name="TEST", item_price=1, item_stock=1, description="TEST", rating=1, item_url="TEST")
        test_data = CatalogItem.objects.get(item_name="TEST")
        self.assertEquals(test_data.item_name, "TEST")
        self.assertEquals(test_data.description, "TEST")