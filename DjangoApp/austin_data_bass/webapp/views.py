from django.shortcuts import render
from django.core.paginator import Paginator
from .gitstats import getGitStats
from .models import Artist
import json
import re
from .models import Venue
from .models import Concerts

from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank

# Create your views here. These are called from urls.py.
# A URL will essentially request a certain "view". Process
# and display that view here. 

#Home page
def home(request):
   	return render(request, 'webapp/index.html')
        
#About page        
def about(request):
	context = getGitStats() #Get git stats from the API
	context['title'] = "About"
	return render(request, 'webapp/about.html', context)


#MODEL PAGES ------------------------------------------------

#Concert grid page
def concerts(request):
	concert_list = Concerts.objects.all()
	#Pagination
	paginator = Paginator(concert_list, 9) #9 Concerts per page
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	context = {
		'concerts': page_obj, #Passing in the concerts on seperate pages
		'model_name' : 'Concerts',
		'title': 'Concerts',
	}
	return render(request, 'webapp/concerts/grid.html', context)

#Concert instance pages
def concert_name(request, concert_name):
	concert = Concerts.objects.filter(concertName__iexact = concert_name).first()
	print(concert.yelpID)
	venue = Venue.objects.filter(yelpID__iexact = concert.yelpID).first()
	if venue is None:
		venue_name = ""
	else:
		venue_name = venue.name #This is used to link to the venue page

	context = {
		'venue_name': venue_name,
		'title': concert_name,
		'concert': concert,
	}
	return render(request, 'webapp/concerts/concert-template.html', context) 

#Artist grid page
def artists(request):
	artist_list = Artist.objects.all()

	#Pagination
	paginator = Paginator(artist_list, 9) #9 Artists per page
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	context = {
		'artists': page_obj, #Passing in the artists on seperate pages
		'model_name' : 'Artists',
		'title': 'Artists',
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
	#Parse the genre list into a more readable format
	for genre in genrestring:
		genre = genre.replace("'", "")
		genre = genre.title()
		if skip:
			skip = False
			continue
		genre = genre[1:]
		genre_list.append(genre)
	genre_list = ", ".join(genre_list)

	artist = Artist.objects.filter(name__iexact = artist_name).first()
	date = Concerts.objects.filter(concertName__iexact = artist.upcomingConcert).first().date
	print(date)
	context = {
		'date' : date,
		'genre' : genre_list,
		'title': artist_name, 
		'artist_name': artist_name,
		'artist': artist, #The __iexact makes querey ignore caps..!
	}
	return render(request, 'webapp/artists/artist-template.html', context)

#Venues grid page
def venues(request):
	venue_list = Venue.objects.all()

	#Pagination
	paginator = Paginator(venue_list, 9) #9 Artists per page
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	context ={
		'venues': page_obj,
		'model_name': 'Venues',
		'title': 'Venues',
	}
	return render(request, 'webapp/venues/grid.html', context)  

#Venue instance template handler
def venue_name(request, venue_name):
	venue = Venue.objects.filter(name__iexact = venue_name).first()
	if venue is None: #If that specific venue wasn't found, just display grid page
		return venues(request)
	#Venue name found, continue on	
	venueName = venue.name
	concerts = Concerts.objects.filter(yelpID = venue.yelpID)
	if concerts is not None:
		upcoming = concerts
	else: 
		upcoming = ""

	context = {
		'upcoming': upcoming,
		'title': venue_name,
		'venue': venue
	}
	return render(request, 'webapp/venues/instance_template.html', context) 


#The querying search results
def search(request):
    #check type (all, artists, concerts, venues)
    model_type = request.GET['type']
    keywords = request.GET['q']
    
    domain = request.META['HTTP_HOST']
    
    artist_vector = SearchVector('name', weight='A' ) + SearchVector('track1', 'track2', 'track3', weight='B') + SearchVector('bio', 'upcomingConcert' , weight='C')    
    concert_vector = SearchVector('concertName', weight='A') + SearchVector('headliner', 'venue', weight='B') + SearchVector('city', weight='C')
    venue_vector = SearchVector('name', weight='A') + SearchVector('location', 'upcomingConcerts', weight='B')
    
    query = SearchQuery(keywords)

    
    #set default values of context
    context = {
        'artist_model': False,
        'concert_model': False,
        'venue_model': False,
        'title': 'Search',
        'domain': domain,
        'keywords': keywords,
        'type': model_type,
    }
    
    if model_type == "All":
        artists = Artist.objects.annotate(rank = SearchRank(artist_vector, query)).filter(rank__gte=0.1).order_by('-rank')
        
        concerts = Concerts.objects.annotate(rank = SearchRank(concert_vector, query)).filter(rank__gte=0.1).order_by('-rank')
        
        venues = Venue.objects.annotate(rank = SearchRank(venue_vector, query)).filter(rank__gte=0.1).order_by('-rank')
        
        #add/update relevant data in context
        context['artist_model'] = True
        context['artists'] = artists
        context['concert_model'] = True
        context['concerts'] = concerts
        context['venue_model'] = True
        context['venues'] = venues
        
        
    elif model_type == "Artists":
        artists = Artist.objects.annotate(rank = SearchRank(artist_vector, query)).filter(rank__gte=0.1).order_by('-rank')
        
        #add/update relevant data in context
        context['artist_model'] = True
        context['artists'] = artists
        
    elif model_type == "Concerts":
        concerts = Concerts.objects.annotate(rank = SearchRank(concert_vector, query)).filter(rank__gte=0.1).order_by('-rank')
        
        #add/update relevant data in context
        context['concert_model'] = True
        context['concerts'] = concerts
        
    elif model_type == "Venues":
        venues = Venue.objects.annotate(rank = SearchRank(venue_vector, query)).filter(rank__gte=0.1).order_by('-rank')
        
        #add/update relevant data in context
        context['venue_model'] = True
        context['venues'] = venues
        
        
    #print(keyword_list)
    #search the types specified (case switch)

    return render(request, 'webapp/search_results/grid.html', context)

#Development view... just for messing around
def dev(request): #Model Grid Page
	context = {
		'artists': Artist.objects.all(), #Is this a list?????
		'model_name' : 'Artists'
	}
	return render(request, 'webapp/artists/artist-template.html', context)      

