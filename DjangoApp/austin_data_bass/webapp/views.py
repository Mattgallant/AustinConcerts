from django.shortcuts import render
from django.core.paginator import Paginator
from .gitstats import getGitStats
from .models import Artist
import json
import re
import datetime
from datetime import time, date, datetime, timedelta
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


# Helper Functions ----------------------------------------

# Split modelList query into pages based on concertsPerPage
def paginate(request, modelList):
	concertsPerPage = 9
	paginator = Paginator(modelList, concertsPerPage)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return page_obj

# Parse genreString into a list of genres in a readable format
def parseGenres(genreString):
	# Get rid of extreneous symbols
	genreString = genreString.replace("[", "")
	genreString = genreString.replace("]", "")
	genreString = genreString.split(",")

	# Parse into a list
	genre_list = []
	skip = True
	for genre in genreString:
		genre = genre.replace("'", "")
		genre = genre.title()
		if skip:
			skip = False
			continue
		genre = genre[1:]
		genre_list.append(genre)
	genre_list = ", ".join(genre_list)
	return genre_list


# MODEL PAGES ------------------------------------------------

#Concert grid page
def concerts(request):
	concert_sort = request.GET.get('sort-select-concert')

	time_filter = request.GET.get('time', '17:00:00')
	date_filter = request.GET.get('date', '00')
	todaySource = datetime.today()

	if time_filter == '17:00:00' and date_filter == '00':
		concert_list = Concerts.objects.filter(date__gte=todaySource.strftime('%Y-%m-%d')).order_by('date')
		for concert in concert_list:
			concert.date = concert.date[5:8]+concert.date[8:]+concert.date[4]+concert.date[0:4]
	elif time_filter != '17:00:00' and date_filter == '00':
		concert_list = Concerts.objects.filter(startingTime= time_filter, date__gte=todaySource.strftime('%Y-%m-%d')).order_by('date')
		for concert in concert_list:
			concert.date = concert.date[5:8]+concert.date[8:]+concert.date[4]+concert.date[0:4]
	elif date_filter !=  '00' and time_filter == '17:00:00':
		if date_filter == '01':
			currentSource = todaySource
		if date_filter == '02':
			currentSource = todaySource + timedelta(days = 7)
		if date_filter == '03':
			currentSource = todaySource + timedelta(days = 14)
		if date_filter == '04':
			currentSource = todaySource + timedelta(days = 21)
		if date_filter == '05':
			currentSource = todaySource + timedelta(days = 28)
		startDate = currentSource.strftime('%Y-%m-%d')
		concert_list = Concerts.objects.filter(date= startDate).order_by('date')
		for x in range(8):
			nextDaySource = currentSource + timedelta(days = x)
			nextDay = nextDaySource.strftime('%Y-%m-%d')
			concert_list = concert_list|Concerts.objects.filter(date = nextDay).order_by('date') 
		for concert in concert_list:
			concert.date = concert.date[5:8]+concert.date[8:]+concert.date[4]+concert.date[0:4]
	else:
		if date_filter == '01':
			currentSource = todaySource
		if date_filter == '02':
			currentSource = todaySource + timedelta(days = 7)
		if date_filter == '03':
			currentSource = todaySource + timedelta(days = 14)
		if date_filter == '04':
			currentSource = todaySource + timedelta(days = 21)
		if date_filter == '05':
			currentSource = todaySource + timedelta(days = 28)
		startDate = currentSource.strftime('%Y-%m-%d')
		concert_list = Concerts.objects.filter(date= startDate,startingTime = time_filter).order_by('date')
		for x in range(8):
			nextDaySource = currentSource + timedelta(days = x)
			nextDay = nextDaySource.strftime('%Y-%m-%d')
			concert_list = concert_list|Concerts.objects.filter(date = nextDay,startingTime = time_filter).order_by('date') 
		for concert in concert_list:
			concert.date = concert.date[5:8]+concert.date[8:]+concert.date[4]+concert.date[0:4]

	if concert_sort == 'Concert Name (A-Z)':
		concert_list = Concerts.objects.all().order_by('concertName')
	elif concert_sort == 'Concert Name (Z-A)':
		concert_list = Concerts.objects.all().order_by('-concertName')
	elif concert_sort == 'Venue Name (A-Z)':
		concert_list = Concerts.objects.all().order_by('venue')
	elif concert_sort == 'Venue Name (Z-A)':
		concert_list = Concerts.objects.all().order_by('-venue')

	context = {
		'concerts': paginate(request, concert_list), #Passing in the concerts on seperate pages
		'model_name' : 'Concerts',
		'title': 'Concerts',
	}
	return render(request, 'webapp/concerts/grid.html', context)

#Concert instance pages
def concert_name(request, concert_name):
	concert = Concerts.objects.filter(concertName__iexact = concert_name).first()
	concert.date = concert.date[5:8]+concert.date[8:]+concert.date[4]+concert.date[0:4]
	remainder = ':00 pm'
	if concert.startingTime[0:2]>='12':
		concert.startingTime = str( int(concert.startingTime[0:2])-12)+remainder
	else :
		concert.startingTime = str( int(concert.startingTime[0:2]))+remainder
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
	artists_sort = request.GET.get('sort-select-artists')

	genre_filter = request.GET.get('genre', 'All')
	popularity_filter = request.GET.get('popularity', 0)

	if genre_filter == 'All' and popularity_filter == 0:
		artist_list = Artist.objects.all()
	elif genre_filter != 'All' and popularity_filter == 0:
		artist_list = Artist.objects.filter(genres__icontains=genre_filter)
	elif popularity_filter != 0 and genre_filter == 'All':
		artist_list = Artist.objects.filter(popularity__gte=popularity_filter)
	else:
		artist_list = Artist.objects.filter(genres__icontains=genre_filter, popularity__gte=popularity_filter)

	if artists_sort == 'Popularity (Decending)':
		artist_list = Artist.objects.all().order_by('-popularity')
	elif artists_sort == 'Popularity (Acending)':
		artist_list = Artist.objects.all().order_by('popularity')
	elif artists_sort == 'Name (A-Z)':
		artist_list = Artist.objects.all().order_by('name')
	elif artists_sort == 'Name (Z-A)':
		artist_list = Artist.objects.all().order_by('-name')
	elif artists_sort == 'Followers (Decending)':
		artist_list = Artist.objects.all().order_by('-followers')
	elif artists_sort == 'Followers (Acending)':
		artist_list = Artist.objects.all().order_by('followers')

	context = {
		'artists': paginate(request, artist_list), 
		'model_name' : 'Artists',
		'title': 'Artists',
	}
	return render(request, 'webapp/artists/grid.html', context)

#Artist instance template
def artist_name(request, artist_name):
	genreString = (Artist.objects.filter(name__iexact = artist_name).first()).genres
	genre_list = parseGenres(genreString)

	artist = Artist.objects.filter(name__iexact = artist_name).first()
	date = Concerts.objects.filter(concertName__iexact = artist.upcomingConcert).first().date

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
	venue_sort = request.GET.get('sort-select-venues')

	rating_filter = request.GET.get('rating', 0)
	cost_filter = request.GET.get('cost', '$')

	if rating_filter == 0 and cost_filter == '$':
		venue_list = Venue.objects.all()
	elif rating_filter != 0 and cost_filter == '$':
		venue_list = Venue.objects.filter(rating__gte= rating_filter)
	elif cost_filter != '$' and rating_filter == 0:
		venue_list = Venue.objects.filter(price=cost_filter)
	else:
		venue_list = Venue.objects.filter(price=cost_filter, rating__gte = rating_filter)

	if venue_sort == 'Venue Name (A-Z)':
		venue_list = Venue.objects.all().order_by('name')
	elif venue_sort == 'Venue Name (Z-A)':
		venue_list = Venue.objects.all().order_by('-name')
	elif venue_sort == 'Yelp Rating (High to Low)':
		venue_list = Venue.objects.all().order_by('rating')
	elif venue_sort == 'Yelp Rating (Low to High)':
		venue_list = Venue.objects.all().order_by('-rating')
	elif venue_sort == 'Price (Low to High)':
		venue_list = Venue.objects.all().order_by('price')
	elif venue_sort == 'Price (High to Low)':
		venue_list = Venue.objects.all().order_by('-price')

	context ={
		'venues': paginate(request, venue_list),
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
#END MODEL PAGES

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
        context['artist_count'] = len(artists)
        context['concert_model'] = True
        context['concerts'] = concerts
        context['concert_count'] = len(concerts)
        context['venue_model'] = True
        context['venues'] = venues
        context['venue_count'] = len(venues)
        
        
    elif model_type == "Artists":
        artists = Artist.objects.annotate(rank = SearchRank(artist_vector, query)).filter(rank__gte=0.1).order_by('-rank')
        
        #add/update relevant data in context
        context['artist_model'] = True
        context['artists'] = artists
        context['artist_count'] = len(artists)

        
    elif model_type == "Concerts":
        concerts = Concerts.objects.annotate(rank = SearchRank(concert_vector, query)).filter(rank__gte=0.1).order_by('-rank')
        
        #add/update relevant data in context
        context['concert_model'] = True
        context['concerts'] = concerts
        context['concert_count'] = len(concerts)

    elif model_type == "Venues":
        venues = Venue.objects.annotate(rank = SearchRank(venue_vector, query)).filter(rank__gte=0.1).order_by('-rank')
        
        #add/update relevant data in context
        context['venue_model'] = True
        context['venues'] = venues
        context['venue_count'] = len(venues)

        
    #print(keyword_list)
    #search the types specified (case switch)

    return render(request, 'webapp/search_results/grid.html', context)
  

