from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(req):
    return render(req, "index.html")


def about(req):
    return HttpResponse("About")


def search(req, keyword, page):
    return HttpResponse(f"Searching for {keyword} on page {page}")


def map(req):
    type = req.GET.get("type", "hybrid")
    lat = req.GET.get("lat", "13.7245601")
    lon = req.GET.get("lon", "100.1930241")
    zoom = req.GET.get("zoom", "18")
    return HttpResponse(f"Map type : {type} lat : {lat} lon : {lon} zoom : {zoom}")
