from django.shortcuts import render
from mywatchlist.models import MyWatchListItem
from django.http import HttpResponse
from django.core import serializers
from .models import MyWatchListItem

def show_home(request):
    watched = MyWatchListItem.objects.filter(watched=True).count()
    not_watched = MyWatchListItem.objects.filter(watched=False).count()
    message = ''
    if (watched > not_watched):
        message = "Selamat, kamu sudah banyak menonton!"
    else:
        message = "Wah, kamu masih sedikit menonton!"

    message_context = {
        'message': message
    }

    return render(request, "home.html", message_context)

def show_mywatchlist_html(request):
    data_mywatchlist = MyWatchListItem.objects.all()
    context = {
        'data_mywatchlist': data_mywatchlist,
        'name': 'Muhammad Hilman Al Ayubi',
        'npm': '2106706653',
    }
    return render(request, "mywatchlist.html", context)

def show_mywatchlist_xml(request):
    data_mywatchlist = MyWatchListItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")

def show_mywatchlist_json(request):
    data_mywatchlist = MyWatchListItem.objects.all()
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")

def show_mywatchlist_xml_by_id(request, id):
    data_mywatchlist_by_id = MyWatchListItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data_mywatchlist_by_id), content_type="application/xml")

def show_mywatchlist_json_by_id(request, id):
    data_mywatchlist_by_id = MyWatchListItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data_mywatchlist_by_id), content_type="application/json")

def update(request, id):
    mywatchlist = MyWatchListItem.objects.get(pk=id)
    mywatchlist.watched = not mywatchlist.watched
    mywatchlist.save()
    return JsonResponse({"instance": "Status diupdate"}, status=200) 