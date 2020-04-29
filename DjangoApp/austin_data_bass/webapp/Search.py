from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank
from .models import Artist, Concerts, Venue

class Search:
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
        
        searcher = _get_searcher(model_type)
        
        return searcher(query, context)
    
def _get_searcher(model_type):
    if model_type == "All":
        return _search_all
    elif model_type == "Artists":
        return _search_artists
    elif model_type == "Concerts":
        return _search_concerts
    elif model_type == "Venues":
        return _search_venues
    else:
        raise ValueError(model_type)


def _search_all(query, context):    
    _search_artists(query, context)
    _search_concerts(query, context)
    _search_venues(query, context)
    
    return context

def _search_artists(query, context):
    artist_vector = SearchVector('name', weight='A' ) + SearchVector('track1', 'track2', 'track3', weight='B') + SearchVector('bio', 'upcomingConcert' , weight='C')    
    artists = Artist.objects.annotate(rank = SearchRank(artist_vector, query)).filter(rank__gte=0.1).order_by('-rank')

    #add/update relevant data in context
    context['artist_model'] = True
    context['artists'] = artists
    context['artist_count'] = len(artists)
    
    return context

def _search_concerts(query, context):
    concert_vector = SearchVector('concertName', weight='A') + SearchVector('headliner', 'venue', weight='B') + SearchVector('city', weight='C')
    concerts = Concerts.objects.annotate(rank = SearchRank(concert_vector, query)).filter(rank__gte=0.1).order_by('-rank')

    #add/update relevant data in context
    context['concert_model'] = True
    context['concerts'] = concerts
    context['concert_count'] = len(concerts)
    return context

def _search_venues(query, context):
    venue_vector = SearchVector('name', weight='A') + SearchVector('location', 'upcomingConcerts', weight='B')
    venues = Venue.objects.annotate(rank = SearchRank(venue_vector, query)).filter(rank__gte=0.1).order_by('-rank')

    #add/update relevant data in context
    context['venue_model'] = True
    context['venues'] = venues
    context['venue_count'] = len(venues)
    return context
