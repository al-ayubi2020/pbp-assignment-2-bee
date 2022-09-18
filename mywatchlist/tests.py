from django.test import TestCase, Client
from django.urls import reverse, resolve
from mywatchlist.views import show_mywatchlist_html
class TestUrls(TestCase):

    def setUp(self):
        self.c = Client()
        self.url_html = reverse('mywatchlist:show_mywatchlist_html')
        self.url_json = reverse('mywatchlist:show_mywatchlist_json')
        self.url_xml = reverse('mywatchlist:show_mywatchlist_xml')

    def test_urls_html_http(self):
        response = self.c.get(self.url_html)
        self.assertEquals(response.status_code , 200)

    def test_urls_json_http(self):
        response = self.c.get(self.url_json)
        self.assertEquals(response.status_code , 200)

    def test_urls_xml_http(self):
        response = self.c.get(self.url_xml)
        self.assertEquals(response.status_code , 200)