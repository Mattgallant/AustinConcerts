from django.test import TestCase
import sys
import json
#import unittest
#from app.main import *
from django.urls import reverse


from django.db import models
import webapp.views

# go to /webapp/migrations and delete all files here and in pycache


class ViewsTest(TestCase):
	def test_home(self):
		url = reverse('webapp-home')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertIn(b"carousel", response.content) #response.content returns html

	def test_artists(self):
		url = reverse('webapp-artists')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertIn(b"Artists", response.content)

	def test_venues(self):
		url = reverse('webapp-venues')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertIn(b"Venues", response.content)

	def test_concerts(self):
		url = reverse('webapp-concerts')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertIn(b"Concerts", response.content)

	def test_about(self):
		url = reverse('webapp-about')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertIn(b"About Us", response.content)


	'''
	def test_search(self):
		url = reverse('webapp-search')
		url += "?type=All&q=band"
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)'''

	
