from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
import pytz
import datetime
import base64
import requests
def index(request):
    if request.method == "POST" and "image" in request.FILES:
        inputname = request.POST['inputname']
        photo=request.FILES["image"].read()
        encoded_string = base64.b64encode(photo)
        photo = encoded_string.decode('ascii')
        p = Post(date=datetime.datetime.now(), photo=photo, name =inputname )
        p.save(force_insert=True)
        pass
    posts = Post.objects.filter().order_by('-date')
    return render(request, 'index.html', {'posts':posts})

def random_picture():
    url = "https://source.unsplash.com/random/400x400"
    response = requests.get(url, stream=True)
    # print(response.content)
    encoded_string = base64.b64encode(response.content)
    del response
    return encoded_string.decode('ascii')
