from django.test import TestCase, Client
from django.urls import reverse, resolve
from mywatchlist.views import show_mywatchlist_html
class TestUrls(TestCase):

    def test_urls_html_http(self):
        c = Client()
        url = reverse('mywatchlist:show_mywatchlist_html')
        response = c.get(url)
        self.assertEquals(response.status_code , 200)
        
    # def test_urls_html(self):
    #     c = Client()
    #     url = reverse('mywatchlist:show_mywatchlist_html')
    #     self.assertEquals(resolve(url).func, show_mywatchlist_html)

    def test_urls_json_http(self):
        c = Client()
        url = reverse('mywatchlist:show_mywatchlist_json')
        response = c.get(url)
        self.assertEquals(response.status_code , 200)

    def test_urls_xml_http(self):
        c = Client()
        url = reverse('mywatchlist:show_mywatchlist_xml')
        response = c.get(url)
        self.assertEquals(response.status_code , 200)