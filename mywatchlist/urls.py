from django.urls import path
from mywatchlist.views import show_mywatchlist_html, show_mywatchlist_json, show_mywatchlist_json_by_id, show_mywatchlist_xml, show_mywatchlist_xml_by_id, show_home

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_home, name='show_home'),
    path('html/', show_mywatchlist_html, name='show_mywatchlist_html'),
    path('xml/', show_mywatchlist_xml, name='show_mywatchlist_xml'),
    path('json/', show_mywatchlist_json, name='show_mywatchlist_json'),
    path('xml/<int:id>', show_mywatchlist_xml_by_id, name='show_mywatchlist_xml_by_id'),
    path('json/<int:id>', show_mywatchlist_json_by_id, name='show_mywatchlist_json_by_id'),
]