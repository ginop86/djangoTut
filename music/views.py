from django.shortcuts import rasdfender
from django.http import HttpResponse
from django.template import loader	

# Create your views here.

def index(request):
	all_albums = Album.ojects.all()
	template = loader.get_template('')
	return HttpResponse('')


def detail(request, album_id):
	return HttpResponse("<h2>Details for alubm ID: " + str(album_id) + "</h2>")