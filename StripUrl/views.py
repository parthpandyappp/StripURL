from django.shortcuts import render
import pyshorteners
import pyqrcode
import png
from pyqrcode import QRCode
import shutil
import os

# Create your views here.


def index(request):
    return render(request, "StripUrl/index.html")


def process(request):
    if request.method == "POST":
        link = request.POST['link']
        shortner = pyshorteners.Shortener()
        x = shortner.tinyurl.short(link)
        url = pyqrcode.create(x)
        url.svg("myqr.svg", scale=8)
        return render(request, "StripUrl/see.html", {'short': x})

    else:
        return render(request, "StripUrl/see.html")
