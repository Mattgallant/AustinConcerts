from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank
from .models import Artist, Concerts, Venue
from abc import ABC, abstractmethod

class SearchFactory:
    def get_search_results(request):
        model_type = request.GET['type']
        keywords = request.GET['q']
        domain = request.META['HTTP_HOST']
        query = SearchQuery(keywords)        
        context = {
            'artist_model': False,
            'concert_model': False,
            'venue_model': False,
            'title': 'Search',
            'domain': domain,
            'keywords': keywords,
            'type': model_type,
        }
        
        searcher = SearchFactory.create_searcher(model_type)
        
        return searcher(query, context)
    
    def create_searcher(model_type):
        if model_type == "All":
            return SearchAll
        elif model_type == "Artists":
            return SearchArtists
        elif model_type == "Concerts":
            return SearchConcerts
        elif model_type == "Venues":
            return SearchVenues
        else:
            raise ValueError(model_type)
            
class Searcher(ABC):    
    def __init__(self):
        self.context = {}
        

    
class SearchAll(Searcher):
    def __init__(self, query, context): 
        SearchArtists(query, context)
        SearchConcerts(query, context)
        SearchVenues(query, context)
        
        self.context = context

class SearchArtists(Searcher):
    def __init__(self, query, context):
        artist_vector = SearchVector('name', weight='A' ) + SearchVector('track1', 'track2', 'track3', weight='B') + SearchVector('bio', 'upcomingConcert' , weight='C')    
        artists = Artist.objects.annotate(rank = SearchRank(artist_vector, query)).filter(rank__gte=0.1).order_by('-rank')

        #add/update relevant data in context
        context['artist_model'] = True
        context['artists'] = artists
        context['artist_count'] = len(artists)
        
        self.context = context


class SearchConcerts(Searcher):
    def __init__(self, query, context):
        concert_vector = SearchVector('concertName', weight='A') + SearchVector('headliner', 'venue', weight='B') + SearchVector('city', weight='C')
        concerts = Concerts.objects.annotate(rank = SearchRank(concert_vector, query)).filter(rank__gte=0.1).order_by('-rank')

        #add/update relevant data in context
        context['concert_model'] = True
        context['concerts'] = concerts
        context['concert_count'] = len(concerts)
        
        self.context = context
        
        
class SearchVenues(Searcher):
    def __init__(self, query, context):
        venue_vector = SearchVector('name', weight='A') + SearchVector('location', 'upcomingConcerts', weight='B')
        venues = Venue.objects.annotate(rank = SearchRank(venue_vector, query)).filter(rank__gte=0.1).order_by('-rank')

        #add/update relevant data in context
        context['venue_model'] = True
        context['venues'] = venues
        context['venue_count'] = len(venues)
        
        self.context = context
        
