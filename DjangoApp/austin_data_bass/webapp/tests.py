from django.test import TestCase
import sys
import json
import unittest

sys.path.append("../..")
from app.main import *

# Create your tests here.

class TestFunctions(unittest.TestCase):
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
	
