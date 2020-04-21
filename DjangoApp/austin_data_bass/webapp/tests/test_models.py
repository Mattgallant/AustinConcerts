from django.test import TestCase
import sys
import json
#import unittest
#from app.main import *

from django.db import models
from webapp.models import Artist, Venue, Concerts

# go to /webapp/migrations and delete all files here and in pycache


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

	def test_artist_popularity(self):
		artist = Artist.create("kesha", "ACL")
		result = artist.popularity
		self.assertTrue(isinstance(result, int))

	def test_artist_followers(self):
		artist = Artist.create("kesha", "ACL")
		result = artist.followers
		self.assertTrue(isinstance(result, int))

	def test_artist_spotifyID(self):
		artist = Artist.create("kesha", "ACL")
		result = artist.spotifyID
		self.assertTrue(isinstance(result, str))

	def test_artist_spotifyLink(self):
		artist = Artist.create("kesha", "ACL")
		result = artist.spotifyLink
		self.assertTrue(isinstance(result, str))

	def test_artist_imageLink(self):
		artist = Artist.create("kesha", "ACL")
		result = artist.imageLink
		self.assertTrue(isinstance(result, str))

	def test_artist_track1(self):
		artist = Artist.create("kesha", "ACL")
		result = artist.track1
		self.assertEqual(result, "TiK ToK")

	def test_artist_track1popularity(self):
		artist = Artist.create("kesha", "ACL")
		result = artist.track1popularity
		self.assertEqual(result, 80)

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

	def test_venue_price(self):
		venue = Venue.create("xaTGgwLwFGopzr1VlpBuBw", "ACL")
		result = venue.price
		self.assertTrue(isinstance(result, str))

	def test_venue_phone(self):
		venue = Venue.create("xaTGgwLwFGopzr1VlpBuBw", "ACL")
		result = venue.phone
		self.assertTrue(isinstance(result, str))
	
	def test_venue_rating(self):
		venue = Venue.create("xaTGgwLwFGopzr1VlpBuBw", "ACL")
		result = venue.rating
		self.assertTrue(isinstance(result, float))

	def test_venue_yelpID(self):
		venue = Venue.create("xaTGgwLwFGopzr1VlpBuBw", "ACL")
		result = venue.yelpID
		self.assertTrue(isinstance(result, str))

	def test_venue_imageURL(self):
		venue = Venue.create("xaTGgwLwFGopzr1VlpBuBw", "ACL")
		result = venue.imageURL
		self.assertTrue(isinstance(result, str))

	def test_venue_yelpURL(self):
		venue = Venue.create("xaTGgwLwFGopzr1VlpBuBw", "ACL")
		result = venue.yelpURL
		self.assertTrue(isinstance(result, str))

	def test_venue_location(self):
		venue = Venue.create("xaTGgwLwFGopzr1VlpBuBw", "ACL")
		result = venue.location
		self.assertTrue(isinstance(result, str))

	def test_venue_latitude(self):
		venue = Venue.create("xaTGgwLwFGopzr1VlpBuBw", "ACL")
		result = venue.latitude
		self.assertTrue(isinstance(result, float))

	def test_venue_longitude(self):
		venue = Venue.create("xaTGgwLwFGopzr1VlpBuBw", "ACL")
		result = venue.longitude
		self.assertTrue(isinstance(result, float))

class ConcertTest(TestCase):

	def test_concert_concertName(self):
		concert_list = Concerts.create(Concerts, "2020-04-25", "2020-05-25")
		concert = concert_list[1]
		result = concert.concertName
		#self.assertEqual(result, "Tattoo @ Diablo Rojo - Guadalupe 2020")
		self.assertEqual(result, "3LAU at Vulcan Gas Company")
	
	def test_concert_city(self):
		concert_list = Concerts.create(Concerts, "2020-04-25", "2020-05-25")
		concert = concert_list[1]
		result = concert.city
		self.assertEqual(result, "Austin, TX, US")
	
	def test_concert_date(self):
		concert_list = Concerts.create(Concerts, "2020-04-25", "2020-05-25")
		concert = concert_list[1]
		result = concert.date
		self.assertEqual(result, "2020-04-25")
	
	def test_concert_headliner(self):
		concert_list = Concerts.create(Concerts, "2020-04-25", "2020-05-25")
		concert = concert_list[1]
		result = concert.headliner
		self.assertEqual(result, "3LAU")
	
	def test_concert_venue(self):
		concert_list = Concerts.create(Concerts, "2020-04-25", "2020-05-25")
		concert = concert_list[1]
		result = concert.venue
		self.assertEqual(result, "Vulcan Gas Company")

	
