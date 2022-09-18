from django.shortcuts import render
from mywatchlist.models import MyWatchListItem
from django.http import HttpResponse
from django.core import serializers

def show_home(request):
    return render(request, "home.html", context)

def show_mywatchlist_html(request):
    return render(request, "mywatchlist.html", context)

def show_mywatchlist_xml(request):
    return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")

def show_mywatchlist_json(request):
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")

def show_mywatchlist_xml_by_id(request, id):
    data_mywatchlist_by_id = MyWatchListItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data_mywatchlist_by_id), content_type="application/xml")

def show_mywatchlist_json_by_id(request, id):
    data_mywatchlist_by_id = MyWatchListItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data_mywatchlist_by_id), content_type="application/json")

watched = MyWatchListItem.objects.filter(watched=True).count()
not_watched = MyWatchListItem.objects.filter(watched=False).count()
message = ''
if (watched > not_watched):
    message = "Selamat, kamu sudah banyak menonton!"
else:
    message = "Wah, kamu masih sedikit menonton!"

data_mywatchlist = MyWatchListItem.objects.all()
context = {
    'data_mywatchlist': data_mywatchlist,
    'name': 'Muhammad Hilman Al Ayubi',
    'npm': '2106706653',
    'message': message,
}