from django.shortcuts import render
from django.core.paginator import Paginator
from .gitstats import getGitStats
from .models import Artist
import json
import re
from .models import Venue
from .models import Concerts
from webapp.Filter import Filter
from webapp.Sort import Sort
from webapp.Search import Searcher, SearchAll, SearchArtists, SearchConcerts, SearchVenues


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
	filter = Filter()
	sort = Sort()

	concert_list = filter.filterConcert(request)
	concert_list = sort.sortConcert(concert_list, request)

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
	filter = Filter()
	sort = Sort()

	artist_list = filter.filterArtist(request)
	artist_list = sort.sortArtist(artist_list, request)

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
	filter = Filter()
	sort = Sort()

	venue_list = filter.filterVenue(request)
	venue_list = sort.sortVenue(venue_list, request)

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
    #context = Search.get_search_results(request)
    #print("test")
    model_type = request.GET['type']
    
    if model_type == "All":
        context = SearchAll(request).get_search_results()
    elif model_type == "Artists":
        context = SearchArtists(request).get_search_results()
    elif model_type == "Concerts":
        context = SearchConcerts(request).get_search_results()
    elif model_type == "Venues":
        context = SearchVenues(request).get_search_results()
    else:
        raise ValueError(model_type)
        
    
    #print(keyword_list)
    #search the types specified (case switch)
    return render(request, 'webapp/search_results/grid.html', context)


  

