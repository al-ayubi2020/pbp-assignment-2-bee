from django.urls import path
from mywatchlist.views import show_mywatchlist_html, show_mywatchlist_json, show_mywatchlist_json_by_id, show_mywatchlist_xml, show_mywatchlist_xml_by_id, show_home, update

app_name = 'mywatchlist'

urlpatterns = [
    path('json/', show_mywatchlist_json, name='show_mywatchlist_json'),
    path('json/<int:id>', show_mywatchlist_json_by_id, name='show_mywatchlist_json_by_id'),
    path('json/update/<int:id>', update, name='update'),
]