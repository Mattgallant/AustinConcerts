from .models import Venue
from .models import Concerts
from .models import Artist
import datetime
from datetime import time, date, datetime, timedelta

class Filter:
	def filterArtist(self, request):
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

		return artist_list

	def filterConcert(self, request):
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

		return concert_list


	def filterVenue(self, request):
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

		return venue_list