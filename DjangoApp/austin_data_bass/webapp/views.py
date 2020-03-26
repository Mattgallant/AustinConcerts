from django.shortcuts import render
from django.http import HttpResponse
import requests
import json


instance_list = [ #List of dictionaries, this stuff gets passed into the grid_template and inserted into cards
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

def getGitStats():
	#Getting commit stats
	response = requests.get("https://api.github.com/repos/mattgallant/AustinConcerts/stats/contributors")
	data = response.json()

	commits = zanderCommits = guyCommits = mattCommits = dylanCommits = willCommits = michaelCommits = 0;
	for i in data:
		if(i.get("author").get("login") == "zandertedjo"):
			zanderCommits = i.get("total")
		if(i.get("author").get("login") == "farmerguycf"):
			guyCommits = i.get("total")
		if(i.get("author").get("login") == "Mattgallant"):
			mattCommits = i.get("total")
		if(i.get("author").get("login") == "dylanwolford"):
			dylanCommits = i.get("total")
		if(i.get("author").get("login") == "michaelhilborn"):
			michaelCommits = i.get("total")
		if(i.get("author").get("login") == "willworthington"):
			willCommits = i.get("total")
		commits += i.get("total")


	#Getting issues stats
	response = requests.get("https://api.github.com/repos/mattgallant/AustinConcerts/issues")
	data = response.json()

	issues = zanderIssues = guyIssues = mattIssues = dylanIssues = willIssues = michaelIssues = 0;
	for i in data:
		if(i.get("user").get("login") == "zandertedjo"):
		    zanderIssues += 1
		if(i.get("user").get("login") == "farmerguycf"):
		    guyIssues += 1
		if(i.get("user").get("login") == "Mattgallant"):
		    mattIssues += 1
		if(i.get("user").get("login") == "dylanwolford"):
		    dylanIssues += 1
		if(i.get("user").get("login") == "michaelhilborn"):
		    michaelIssues += 1
		if(i.get("user").get("login") == "willworthington"):
		    willIssues+= 1

	ret_dict ={
		'totalCommits' : commits,
		'zanderCommits' : zanderCommits,
		'mattCommits' : mattCommits,
		'guyCommits' : guyCommits,
		'willCommits' : willCommits,
		'michaelCommits' : michaelCommits,
		'dylanCommits': dylanCommits,
		'totalIssues' : data.get("number"),
		'michaelIssues': michaelIssues,
		'zanderIssues': zanderIssues,
		'mattIssues': mattIssues,
		'guyIssues': guyIssues,
		'willIssues': willIssues,
		'dylanIssues': dylanIssues
	}
	#print(ret_dict)
	return ret_dict
        
def about(request):
	context = getGitStats() #Need to pass this in
	context['title'] = "About"
	return render(request, 'webapp/about.html', context)

def concerts(request):
    return render(request, 'webapp/concerts/index.html', {'title': 'Concerts'})

def artists(request):
  	return render(request, 'webapp/artists/index.html', {'title': 'Artists'})

def venues(request):
    return render(request, 'webapp/venues/index.html', {'title': 'Venues'})  

def dev(request): #Model Grid Page
    context = {
	    'instances' : instance_list,
	   	'model_name' : 'Venues'
	}
    return render(request, 'webapp/grid_template.html', context)      

def venues_template(request):
    context = { #Below are the areas you can populate by sending in values
        'title' : 'Venue Name',
        'address' : '123 Big Road',
        'phone' : '512-999-8888',
        'website' : 'www.google.com',
        'review' : '4.0',
        'review_count' : '50'
	}
    return render(request, 'webapp/venues/instances/instance_template.html', context)  
