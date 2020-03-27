from django.shortcuts import render
from django.http import HttpResponse
from .gitstats import getGitStats
from .models import Artist
import json
import re
from .models import Venue


instance_list = [ #List of dictionaries, this stuff gets passed into the grid_template and inserted into cards
	{
		'name': 'The Venue',
		'attri1': '123 abc Rd.',
		'attri2': '1000',
		'attri3': '4.0/5.0'
	},
	{
		'name': 'Mutt',
		'attri1': 'Blog Post 2',
		'attri2': 'First post BUT NOT REALLY',
		'attri3': 'Jan 7th 2020'
	},
	{
		'name': 'The Venue',
		'attri1': '123 abc Rd.',
		'attri2': '1000',
		'attri3': '4.0/5.0'
	},
	{
		'name': 'The Venue',
		'attri1': '123 abc Rd.',
		'attri2': '1000',
		'attri3': '4.0/5.0'
	},
	{
		'name': 'The Venue',
		'attri1': '123 abc Rd.',
		'attri2': '1000',
		'attri3': '4.0/5.0'
	},
	{
		'name': 'The Venue',
		'attri1': '123 abc Rd.',
		'attri2': '1000',
		'attri3': '4.0/5.0'
	},
	{
		'name': 'The Venue',
		'attri1': '123 abc Rd.',
		'attri2': '1000',
		'attri3': '4.0/5.0'
	},
	{
		'name': 'The Venue',
		'attri1': '123 abc Rd.',
		'attri2': '1000',
		'attri3': '4.0/5.0'
	},
	{
		'name': 'The Venue',
		'attri1': '123 abc Rd.',
		'attri2': '1000',
		'attri3': '4.0/5.0'
	},
]

# Create your views here. These are called from urls.py.
# A URL will essentially request a certain "view". Process
# and display that view here. 
def home(request):
   	return render(request, 'webapp/index.html')
        
def about(request):
	context = getGitStats() #Get git stats from the API
	context['title'] = "About"
	return render(request, 'webapp/about.html', context)

def concerts(request):
    return render(request, 'webapp/concerts/grid.html', {'title': 'Concerts'})

#Artist grid page
"""	artist_list = Artist.objects.all()
	print(type(list(artist_list)))
	for artist in artist_list:
		genrestring = artist['genres']
		genrestring = genrestring.replace("[", "")
		genrestring = genrestring.replace("]", "")
		genrestring = genrestring.split(",")
		genre_list = []
		skip = True
		for genre in genrestring:
			genre = genre.replace("'", "")
			genre = genre.title()
			if skip:
				skip = False
				continue
			genre = genre[1:]
			genre_list.append(genre)
		genre_list = ", ".join(genre_list)
		artist['genres'] = genre_list"""
def artists(request):
	context = {
		'artists': Artist.objects.all(), #Is this a list?????
		'model_name' : 'Artists',
		'title': 'Artists'
	}
	return render(request, 'webapp/artists/grid.html', context)

#Artist instance template
def artist_name(request, artist_name):
#Query the database, filter by artist_name
#Get relevant instance info, pass to template
	#Handle genre string
	genrestring = (Artist.objects.filter(name__iexact = artist_name).first()).genres
	genrestring = genrestring.replace("[", "")
	genrestring = genrestring.replace("]", "")
	genrestring = genrestring.split(",")
	genre_list = []
	skip = True
	for genre in genrestring:
		genre = genre.replace("'", "")
		genre = genre.title()
		if skip:
			skip = False
			continue
		genre = genre[1:]
		genre_list.append(genre)
	genre_list = ", ".join(genre_list)

	context = {
		'genre' : genre_list,
		'title': artist_name, 
		'artist_name': artist_name,
		'artist': Artist.objects.filter(name__iexact = artist_name).first(), #The __iexact makes querey ignore caps..!
	}
	return render(request, 'webapp/artists/artist-template.html', context)

def venues(request):
	context ={
		'venues': Venue.objects.all(),
		'model_name': 'Venues',
		'title': 'Venues',
	}
	return render(request, 'webapp/venues/grid.html', context)  

#Venue instance template handler
def venue_name(request, venue_name):
	context = {
		'title': venue_name,
		'venue': Venue.objects.filter(name__iexact = venue_name).first(),
	}
	return render(request, 'webapp/venues/instance_template.html', context) 

def dev(request): #Model Grid Page
	"""    context = {
	    'instances' : instance_list,
	   	'model_name' : 'Venues'
	}"""
	context = {
		'artists': Artist.objects.all(), #Is this a list?????
		'model_name' : 'Artists'
	}
	return render(request, 'webapp/artists/artist-template.html', context)      

def venues_template(request):
    context = { #Below are the areas you can populate by sending in values
        'title' : 'Venue Name',
        'address' : '123 Big Road',
        'phone' : '512-999-8888',
        'website' : 'www.google.com',
        'review' : '4.0',
        'review_count' : '50'
	}
    return render(request, 'webapp/venues/instances/instance_template.html', context)  
