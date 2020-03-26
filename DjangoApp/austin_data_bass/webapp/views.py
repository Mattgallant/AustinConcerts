from django.shortcuts import render
from django.http import HttpResponse


instance_list = [ #List of dictionaries
	{
		'name': 'The Venue',
		'attri1': '123 abc Rd.',
		'attri2': '1000',
		'attri3': '4.0/5.0'
	},
	{
		'name': 'Mutt',
		'attri1': 'Blog Post 2',
		'attri2': 'First post BUT NOT REALLY',
		'attri3': 'Jan 7th 2020'
	},
	{
		'name': 'The Venue',
		'attri1': '123 abc Rd.',
		'attri2': '1000',
		'attri3': '4.0/5.0'
	},
	{
		'name': 'The Venue',
		'attri1': '123 abc Rd.',
		'attri2': '1000',
		'attri3': '4.0/5.0'
	},
	{
		'name': 'The Venue',
		'attri1': '123 abc Rd.',
		'attri2': '1000',
		'attri3': '4.0/5.0'
	},
	{
		'name': 'The Venue',
		'attri1': '123 abc Rd.',
		'attri2': '1000',
		'attri3': '4.0/5.0'
	},
	{
		'name': 'The Venue',
		'attri1': '123 abc Rd.',
		'attri2': '1000',
		'attri3': '4.0/5.0'
	},
	{
		'name': 'The Venue',
		'attri1': '123 abc Rd.',
		'attri2': '1000',
		'attri3': '4.0/5.0'
	},
	{
		'name': 'The Venue',
		'attri1': '123 abc Rd.',
		'attri2': '1000',
		'attri3': '4.0/5.0'
	},
]

# Create your views here. These are called from urls.py.
# A URL will essentially request a certain "view". Process
# and display that view here. 
def home(request):
    return render(request, 'webapp/index.html')

def about(request):
    return render(request, 'webapp/about.html', {'title': 'About'})

def concerts(request):
    return render(request, 'webapp/concerts/index.html', {'title': 'Concerts'})

def artists(request):
    return render(request, 'webapp/artists/index.html', {'title': 'Artists'})

def venues(request):
    return render(request, 'webapp/venues/index.html', {'title': 'Venues'})  

def dev(request):
    context = {
	    'instances' : instance_list,
	    'model_name' : 'Venues'
	}
    return render(request, 'webapp/grid_template.html', context)      