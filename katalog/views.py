from django.shortcuts import render
from katalog.models import CatalogItem
from django.template import loader
from django.http import HttpResponse

def show_catalog(request):
    return render(request, "katalog.html", context)

data_catalog = CatalogItem.objects.all()
context = {
    'data_catalog': data_catalog,
    'name': 'Muhammad Hilman Al Ayubi',
    'npm': '2106706653'
}
