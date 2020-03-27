from django.shortcuts import render
from django.http import HttpResponse
from .gitstats import getGitStats
from .models import Artist


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
    return render(request, 'webapp/concerts/index.html', {'title': 'Concerts'})

def artists(request):
  	return render(request, 'webapp/artists/index.html', {'title': 'Artists'})

def artist_name(request, artist_name):
  	return render(request, 'webapp/artists/index.html', {'title': artist_name, 'artist_name': artist_name})

def venues(request):
    return render(request, 'webapp/venues/index.html', {'title': 'Venues'})  

def dev(request): #Model Grid Page
	"""    context = {
	    'instances' : instance_list,
	   	'model_name' : 'Venues'
	}"""
	context = {
		'artists': Artist.objects.all(), #Is this a list?????
		'model_name' : 'Artists'
	}
	return render(request, 'webapp/grid_template.html', context)      

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
