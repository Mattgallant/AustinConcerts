from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank
from .models import Artist, Concerts, Venue
from abc import ABC, abstractmethod

            
class Searcher(ABC):    
    
    def __init__(self, request):
        model_type = request.GET['type']
        keywords = request.GET['q']
        domain = request.META['HTTP_HOST']
        self.query = SearchQuery(keywords)        
        self.context = {
            'artist_model': False,
            'concert_model': False,
            'venue_model': False,
            'title': 'Search',
            'domain': domain,
            'keywords': keywords,
            'type': model_type,
        }
    
    def get_search_results(self):
        self.doSearch()
        self.setContext()
        return self.context
        
    @abstractmethod
    def doSearch(self):
        pass
    
    
    @abstractmethod
    def setContext(self):
        pass
        
    
class SearchAll(Searcher):
    def doSearch(self):
        SearchArtists.doSearch(self)
        SearchConcerts.doSearch(self)
        SearchVenues.doSearch(self)
        
    def setContext(self):
        SearchArtists.setContext(self)
        SearchConcerts.setContext(self)
        SearchVenues.setContext(self)

class SearchArtists(Searcher):
    def doSearch(self):
        artist_vector = SearchVector('name', weight='A' ) + SearchVector('track1', 'track2', 'track3', weight='B') + SearchVector('bio', 'upcomingConcert' , weight='C')    
        self.artists = Artist.objects.annotate(rank = SearchRank(artist_vector, self.query)).filter(rank__gte=0.1).order_by('-rank')

    def setContext(self):
        #add/update relevant data in context
        self.context['artist_model'] = True
        self.context['artists'] = self.artists
        self.context['artist_count'] = len(self.artists)
        

class SearchConcerts(Searcher):
    def doSearch(self):
        concert_vector = SearchVector('concertName', weight='A') + SearchVector('headliner', 'venue', weight='B') + SearchVector('city', weight='C')
        self.concerts = Concerts.objects.annotate(rank = SearchRank(concert_vector, self.query)).filter(rank__gte=0.1).order_by('-rank')

    def setContext(self):
        #add/update relevant data in context
        self.context['concert_model'] = True
        self.context['concerts'] = self.concerts
        self.context['concert_count'] = len(self.concerts)
        
        
class SearchVenues(Searcher):
    def doSearch(self):
        venue_vector = SearchVector('name', weight='A') + SearchVector('location', 'upcomingConcerts', weight='B')
        self.venues = Venue.objects.annotate(rank = SearchRank(venue_vector, self.query)).filter(rank__gte=0.1).order_by('-rank')

    def setContext(self):
        #add/update relevant data in context
        self.context['venue_model'] = True
        self.context['venues'] = self.venues
        self.context['venue_count'] = len(self.venues)
                
