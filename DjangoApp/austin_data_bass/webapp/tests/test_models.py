from django.test import TestCase
import sys
import json
#import unittest

#sys.path.append("../..")
#from app.main import *

# Create your tests here.

'''class TestFunctions(unittest.TestCase):
	"""test case for cient methods"""
	def setup(self):
		app.app.config['TESTING'] = True
		self.app = app.app.test_client()

	# Test of output function
	def test_output(self):		# CHANGE TO SPECIFIC OBJECT
		with app.test_request_context():
			# mock object
			out = output('error', 'Test Error', 'local_host') # CHANGE TO SPECIFIC OBJECT
			# passing the mock object
			response = [
				{
					'type': 'error',	# CHANGE TO SPECIFIC OBJECT
					'message': 'Test Error',
					'download_link': 'local_host'
				}
			]
			data = json.loads(out.get_data(as_text=True))
			# assert response
			self.assertEqual(data['response'], response)


if __name__ == '__main__':
	unittest.main()
	'''

from django.db import models
from webapp.models import Artist, Venue, Concerts

class ArtistTest(TestCase):
	def test_artist_name(self):
		artist = Artist.create("kesha", "ACL")
		result = artist.name
		self.assertEqual(result, "Kesha")
	def test_artist_bio(self):
		artist = Artist.create("kesha", "ACL")
		result = artist.bio
		self.assertTrue(isinstance(result, str))
	def test_artist_genres(self):
		artist = Artist.create("kesha", "ACL")
		result = artist.genres
		self.assertTrue(result) #check not empty

class VenueTest(TestCase):
	def test_venue_name(self):
		venue = Venue.create("xaTGgwLwFGopzr1VlpBuBw", "ACL")
		result = venue.name
		self.assertEqual(result, "Mohawk")
	def test_venue_location(self):
		venue = Venue.create("xaTGgwLwFGopzr1VlpBuBw", "ACL")
		result = venue.location
		self.assertEqual(result, "912 Red River St Austin, TX 78701")
	def test_venue_reviewCount(self):
		venue = Venue.create("xaTGgwLwFGopzr1VlpBuBw", "ACL")
		result = venue.reviewCount
		self.assertEqual(result, 243)

class ConcertTest(TestCase):
	def test_concert_concertName(self):
		concert_list = Concerts.create()
		concert = concert_list[0]
		result = concert.concertName
		self.assertEqual(result, "Tattoo @ Diablo Rojo - Guadalupe 2020")
	def test_concert_city(self):
		concert_list = Concerts.create()
		concert = concert_list[0]
		result = concert.city
		self.assertEqual(result, "Austin, TX, US")
	def test_concert_date(self):
		concert_list = Concerts.create()
		concert = concert_list[0]
		result = concert.date
		self.assertEqual(result, "2020-03-28")
	
