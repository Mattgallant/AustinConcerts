from .models import Venue
from .models import Concerts
from .models import Artist

class Sort:
	def sortArtist(self, artist_list, request):
		artists_sort = request.GET.get('sort-select-artists')

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

		return artist_list

	def sortVenue(self, venue_list, request):
		venue_sort = request.GET.get('sort-select-venues')

		if venue_sort == 'Venue Name (A-Z)':
			venue_list = Venue.objects.all().order_by('name')
		elif venue_sort == 'Venue Name (Z-A)':
			venue_list = Venue.objects.all().order_by('-name')
		elif venue_sort == 'Yelp Rating (High to Low)':
			venue_list = Venue.objects.all().order_by('-rating')
		elif venue_sort == 'Yelp Rating (Low to High)':
			venue_list = Venue.objects.all().order_by('rating')
		elif venue_sort == 'Price (Low to High)':
			venue_list = Venue.objects.all().order_by('price')
		elif venue_sort == 'Price (High to Low)':
			venue_list = Venue.objects.all().order_by('-price')

		return venue_list

	def sortConcert(self, concert_list, request):
		concert_sort = request.GET.get('sort-select-concert')

		if concert_sort == 'Concert Name (A-Z)':
			concert_list = Concerts.objects.all().order_by('concertName')
		elif concert_sort == 'Concert Name (Z-A)':
			concert_list = Concerts.objects.all().order_by('-concertName')
		elif concert_sort == 'Venue Name (A-Z)':
			concert_list = Concerts.objects.all().order_by('venue')
		elif concert_sort == 'Venue Name (Z-A)':
			concert_list = Concerts.objects.all().order_by('-venue')

		return concert_list
