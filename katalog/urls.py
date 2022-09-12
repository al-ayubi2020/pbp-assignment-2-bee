# TODO: Implement Routings Here

from django.urls import path
from katalog.views import show_catalog

urlpatterns = [
    path('', show_catalog, name='show_catalog'),
]