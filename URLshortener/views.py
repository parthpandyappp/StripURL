from django.shortcuts import render
import pyshorteners
import pyqrcode
import png
from pyqrcode import QRCode
import shutil
import os

# Create your views here.


def index(request):
    return render(request, "URLshortener/index.html")


def process(request):
    if request.method == "POST":
        link = request.POST['link']
        shortner = pyshorteners.Shortener()
        x = shortner.tinyurl.short(link)
        url = pyqrcode.create(x)
        url.svg("/home/parth/Documents/finale/StripURL/URLshortener/static/images/myqr.svg", scale=8)
        return render(request, "URLshortener/shortened.html", {'short': x})

    else:
        return render(request, "URLshortener/shortened.html")