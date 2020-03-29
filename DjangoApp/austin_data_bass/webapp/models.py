from django.db import models
import requests
import base64
import six
import json
import wikipedia

from django.contrib.postgres.fields import ArrayField
maxbio_length = 997

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=25)
    spotifyID = models.CharField(max_length=50)
    spotifyLink = models.CharField(max_length=200)
    imageLink = models.CharField(max_length=200)
    bio = models.CharField(max_length=1000)
    genres = models.CharField(max_length=150) #will be a json list of genres
    popularity = models.IntegerField()
    followers = models.IntegerField()
    track1 = models.CharField(max_length=50)
    track1popularity = models.CharField(max_length=10)
    track2 = models.CharField(max_length=50) 
    track2popularity = models.CharField(max_length=10)
    track3 = models.CharField(max_length=50) 
    track3popularity = models.CharField(max_length=10)

    
    def __str__(self):
        #This function just allows the model to be displayed in a more readable fashion
        return(self.name)

    def create(artistName):
        #get the token to use the spotify API
        clientId = '7fed28ee3a0d4a89838c1edd4a891b63'
        secret = '492d077d949c4f21a79eedff5d70852d'
        auth = base64.b64encode(
            six.text_type(clientId + ':' + secret).encode("ascii")
            )
        payload = {"grant_type": "client_credentials"}

        resp = requests.post("https://accounts.spotify.com/api/token",
                             data=payload,
                             headers={'Authorization': "Basic %s" % auth.decode("ascii")},
                             verify=True)

        token = resp.json()['access_token']
        
        URL1 = "https://api.spotify.com/v1/search?q=" + artistName.lower().replace(" ", "%20") + "&type=artist"

        r1 = requests.get(url = URL1, headers={'Authorization': 'Bearer ' + token}) 

        data1 = r1.json()['artists']['items'][0]

        artist = {
            'name': data1['name'],
            'spotifyID': data1['uri'][15:],
            'imageLink': data1['images'][0]['url'],
            'spotifyLink': data1['external_urls']['spotify'],
            'bio': '',
            'genres': data1['genres'],
            'popularity': data1['popularity'],
            'followers': data1['followers']['total'],
        }

        URL2 = "https://api.spotify.com/v1/artists/" + artist['spotifyID'] + "/top-tracks?country=US"
        r2 = requests.get(url = URL2, headers={'Authorization': 'Bearer ' + token}) 

        data2 = r2.json()['tracks'][0:3]

        topTracks = []

        for track in data2:
            topTracks.append({'track':track['name'], 'popularity':track['popularity']})

        artist['topTracks'] = topTracks
        
        #now get the artist's wikipedia bio
        bio = wikipedia.summary(artistName + " musician")
        bio_array = bio.splitlines()
        bio_short = bio_array[0][0:maxbio_length] 

        # chop bios that are too long
        if(len(bio_short) >= maxbio_length):
            bio_short = bio_short + '...'
            
        artist['bio'] = bio_short

        
        return Artist(name = artist['name'],
                     spotifyID = artist['spotifyID'],
                     imageLink = artist['imageLink'],
                     spotifyLink = artist['spotifyLink'],
                     bio = artist['bio'],
                     genres = artist['genres'],
                     popularity = artist['popularity'],
                     followers = artist['followers'],
                     track1 = artist['topTracks'][0]['track'],
                     track1popularity = artist['topTracks'][0]['popularity'],
                     track2 = artist['topTracks'][1]['track'],
                     track2popularity = artist['topTracks'][1]['popularity'],
                     track3 = artist['topTracks'][2]['track'],
                     track3popularity = artist['topTracks'][2]['popularity'],)




class Venue(models.Model):
    name = models.CharField(max_length=200)
    yelpID =  models.CharField(max_length=25)
    imageURL = models.CharField(max_length=300)
    yelpURL = models.CharField(max_length=300)
    phone = models.CharField(max_length=15) 
    reviewCount = models.IntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    location = models.CharField(max_length=150)
    latitude = models.DecimalField(max_digits=15, decimal_places=13) 
    longitude = models.DecimalField(max_digits=15, decimal_places=13) 
    price = models.CharField(max_length=4)

    def __str__(self):
        #This function just allows the model to be displayed in a more readable fashion
        return(self.name)


    def create(venueID):
        api_key='a2R0zfYLU_ef2pXcyBp36PgiTP5gYuCUimOnsTOjj9chMB5MpZCYzfE4zULFYknJa9edApMste6zAGjxnLhvrP2Q3EDLvQn7_DDI8qqfb0rTxo3Y3a9J4qIQf19dXnYx'
        headers = {'Authorization': 'Bearer a2R0zfYLU_ef2pXcyBp36PgiTP5gYuCUimOnsTOjj9chMB5MpZCYzfE4zULFYknJa9edApMste6zAGjxnLhvrP2Q3EDLvQn7_DDI8qqfb0rTxo3Y3a9J4qIQf19dXnYx'}
        
        #url = "https://api.yelp.com/v3/businesses/search?location=austin&term=concert venues&limit=50"
        #response = requests.request("GET", url, headers=headers, data = payload)

        #parsed = json.loads(response.text)
        #businesses = parsed["businesses"]
        #id_alias_dict = {}
        #for business in businesses:
            #id_alias_dict[business["id"]] = business["name"]
        

        url = "https://api.yelp.com/v3/businesses/" + venueID
        r1 = requests.request("GET", url, headers=headers, data = {})
        data1 = json.loads(r1.text)
        priceholder = "$$"

        if ("price" in data1):
            priceholder = data1["price"]
        

        venue = {
            "name": data1["name"],
            "yelpID": data1["id"],
            "imageURL": data1["image_url"],
            "yelpURL": data1["url"],
            "phone": data1["display_phone"],
            "reviewCount": data1["review_count"],
            "rating": data1["rating"],
            "location": " ".join(data1["location"]["display_address"]),
            "latitude": data1["coordinates"]["latitude"],
            "longitude": data1["coordinates"]["longitude"],
            "price": priceholder
            
        }


        return Venue(name = venue['name'],
                    yelpID =  venue['yelpID'],
                    imageURL = venue['imageURL'],
                    yelpURL = venue['yelpURL'],
                    phone = venue['phone'],
                    reviewCount = venue['reviewCount'],
                    rating = venue['rating'],
                    location = venue['location'], 
                    latitude = venue['latitude'],
                    longitude = venue['longitude'],
                    price = venue['price'])

    
        
class Concerts(models.Model):
	city = models.CharField(max_length = 200)
	concertName = models.CharField(max_length=200)
	artists = ArrayField(models.CharField(max_length=200), blank = True,size = 80)
	venue = models.CharField(max_length = 200)
	venueWebsite = models.CharField(max_length = 200)
	startingTime = models.CharField(max_length = 200)
	date = models.CharField(max_length = 200)
	
	def __str__(self):
		return self.concertName
	def create():
		
		key = 'fYlpdrJQZavt4FGw'
		locationResponse = requests.get('https://api.songkick.com/api/3.0/search/locations.json?query=Austin&apikey=' +key)

		location = locationResponse.json()
		cityID = str(location['resultsPage']['results']['location'][0]['metroArea']['id'])
		PARAMS = {'min_date': '2020-03-28','max_date': '2020-04-03'}
		eventsResponseDate = requests.get('https://api.songkick.com/api/3.0/metro_areas/'+ cityID+'/calendar.json?apikey='+key, PARAMS)

		eventsForWeek = eventsResponseDate.json()

		eventsWeek = eventsForWeek['resultsPage']['results']['event']

		concerts =[]
		for eachEvent in eventsWeek:
			concertTitle = eachEvent['displayName']
			artist = []
			performances = eachEvent['performance']
			for performance in performances:
				artist.append(performance['displayName'])
			City = eachEvent['location']['city']
			Venue = eachEvent['venue']['displayName']
			VenueWebsite = eachEvent['venue']['uri']
			if VenueWebsite is None:
				VenueWebsite = 'N/A'
			StartingTime = '21:00:00'
			Date = eachEvent['start']['date']
			
			specificConcert = Concerts(city = City,concertName = concertTitle,artists = artist,venue = Venue,venueWebsite = VenueWebsite,startingTime = StartingTime,date = Date)
			concerts.append(specificConcert)
		

		return concerts
