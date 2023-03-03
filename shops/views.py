from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.contrib.gis.geos import fromstr,Point
from django.contrib.gis.db.models.functions import Distance
from .models import Shop
from django.http import HttpResponse
from django.shortcuts import render
from .tasks import *

longitude = 36.8353
latitude = -1.223000

user_location = Point(longitude, latitude, srid=4326)

class Home(generic.ListView):
    model = Shop
    context_object_name = 'shops'
    queryset = Shop.objects.annotate(distance=Distance('location',
    user_location)
    ).order_by('distance')[0:10]
    template_name = 'shops/index.html'

def test(request):
    send_mail_func.delay()
    return HttpResponse('Sent')
