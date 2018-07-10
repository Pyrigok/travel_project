from django.shortcuts import render


from .util import get_albums, get_trips
from .models import Travels_Model

def albums_processor(request):
	return({'ALBUMS': get_albums(request)})

def trips_processor(request):
	return ({'TRIPS': get_trips(request)})