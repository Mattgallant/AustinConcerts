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
		name = models.CharField(max_length=105)
		spotifyID = models.CharField(max_length=100)
		spotifyLink = models.CharField(max_length=200)
		imageLink = models.CharField(max_length=200)
		bio = models.CharField(max_length=1000)
		genres = models.CharField(max_length=200) #will be a json list of genres
		popularity = models.IntegerField()
		followers = models.IntegerField()
		track1 = models.CharField(max_length=105)
		track1popularity = models.CharField(max_length=10)
		track2 = models.CharField(max_length=105) 
		track2popularity = models.CharField(max_length=10)
		track3 = models.CharField(max_length=105) 
		track3popularity = models.CharField(max_length=10)
		upcomingConcert = models.CharField(max_length=200,default = 'N/A')

		def __str__(self):
#This function just allows the model to be displayed in a more readable fashion
				return(self.name)

		def create(artistName, concertName):
#get the token to use the spotify API
				clientId = '7fed28ee3a0d4a89838c1edd4a891b63'
				secret = '492d077d949c4f21a79eedff5d70852d'
				auth = base64.b64encode(six.text_type(clientId + ':' + secret).encode("ascii"))
				payload = {"grant_type": "client_credentials"}
				resp = requests.post("https://accounts.spotify.com/api/token",data=payload,headers={'Authorization': "Basic %s" % auth.decode("ascii")},verify=True)
				token = resp.json()['access_token']
				URL1 = "https://api.spotify.com/v1/search?q=" + artistName.lower().replace(" ", "%20") + "&type=artist"
				r1 = requests.get(url = URL1, headers={'Authorization': 'Bearer ' + token})
				try:
						data1 = r1.json()['artists']['items'][0]
				except:
						return None

				artist = {
						'name': data1['name'],
						'spotifyID': data1['uri'][15:],
						'imageLink': data1['images'][0]['url'],
						'spotifyLink': data1['external_urls']['spotify'],
						'bio': '',
						'genres': data1['genres'],
						'popularity': data1['popularity'],
						'followers': data1['followers']['total'],
						'upcomingConcert': concertName
				}

				URL2 = "https://api.spotify.com/v1/artists/" + artist['spotifyID'] + "/top-tracks?country=US"
				r2 = requests.get(url = URL2, headers={'Authorization': 'Bearer ' + token}) 

				data2 = r2.json()['tracks'][0:3]

				topTracks = []

				count = 0
				for track in data2:
						topTracks.append({'track':track['name'], 'popularity':track['popularity']})
						count = ++count

				for i in range(count, 3):
						topTracks.append({'track':'', 'popularity':''})

				artist['topTracks'] = topTracks

				#now get the artist's wikipedia bio
				try:
						bio = wikipedia.summary(artistName + " musician")
						bio_array = bio.splitlines()
						bio_short = bio_array[0][0:maxbio_length] 

						#chop bios that are too long
						if(len(bio_short) >= maxbio_length):
								bio_short = bio_short + '...'
				except:
						bio_short = "No Wikipedia info found."
				finally:
						artist['bio'] = bio_short

				return Artist(name = artist['name'],
							  spotifyID = artist['spotifyID'],
							  imageLink = artist['imageLink'][0:200],
							  spotifyLink = artist['spotifyLink'][0:199],
							  bio = artist['bio'],
							  genres = artist['genres'][0:199],
							  popularity = artist['popularity'],
							  followers = artist['followers'],
							  track1 = artist['topTracks'][0]['track'],
							  track1popularity = artist['topTracks'][0]['popularity'],
							  track2 = artist['topTracks'][1]['track'],
							  track2popularity = artist['topTracks'][1]['popularity'],
							  track3 = artist['topTracks'][2]['track'],
							  track3popularity = artist['topTracks'][2]['popularity'],
							  upcomingConcert = artist['upcomingConcert'][0:199])


class Venue(models.Model):
        name = models.CharField(max_length=200, default="Insert Name")
        yelpID =  models.CharField(max_length=25, default="Insert yelpID")
        imageURL = models.CharField(max_length=300, default="Insert Image")
        yelpURL = models.CharField(max_length=300, default="Insert Yelp URL")
        phone = models.CharField(max_length=15, default="N/A") 
        reviewCount = models.IntegerField(default=0)
        rating = models.DecimalField(max_digits=2, decimal_places=1, default=2.5)
        location = models.CharField(max_length=150, default="Insert Location")
        latitude = models.DecimalField(max_digits=17, decimal_places=14, default=30.2885) 
        longitude = models.DecimalField(max_digits=17, decimal_places=14, default=97.7355) 
        price = models.CharField(max_length=4, default="$$")
        upcomingConcerts = ArrayField(models.CharField(max_length=200), blank = True, size = 80)

        def __str__(self):
        #This function just allows the model to be displayed in a more readable fashion
                return(self.name)


        def create(venueID, concertName):
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
                phonenumber = "N/A"

                if ("price" in data1):
                        priceholder = data1["price"]

                if ("display_phone" in data1):
                        phonenumber = data1["display_phone"]
                
                try:
                    venue = {"name": data1["name"],
                        "yelpID": data1["id"],
                        "imageURL": data1["image_url"],
                        "yelpURL": data1["url"],
                        "phone": phonenumber,
                        "reviewCount": data1["review_count"],
                        "rating": data1["rating"],
                        "location": " ".join(data1["location"]["display_address"]),
                        "latitude": data1["coordinates"]["latitude"],
                        "longitude": data1["coordinates"]["longitude"],
                        "price": priceholder,
                        "upcomingConcerts": concertName
                        }
                except:
                    return None


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
                        price = venue['price'],
                        upcomingConcerts = venue['upcomingConcerts'])





class Concerts(models.Model):
		city = models.CharField(max_length = 200)
		concertName = models.CharField(max_length=200)
		artists = ArrayField(models.CharField(max_length=200), blank = True,size = 80)
		venue = models.CharField(max_length = 200)
		venueWebsite = models.CharField(max_length = 200)
		startingTime = models.CharField(max_length = 200)
		date = models.CharField(max_length = 200)
		headliner = models.CharField(max_length = 200,default = 'N/A')
		imageURL = models.CharField(max_length = 200,default = 'N/A')					
		yelpID = models.CharField(max_length = 200,default = 'N/A')

		def __str__(self):
				return self.concertName
			#spotify API info to get artist image
		def create(self, startDate,endDate):
                    clientId = '7fed28ee3a0d4a89838c1edd4a891b63'
                    secret = '492d077d949c4f21a79eedff5d70852d'
                    auth = base64.b64encode(six.text_type(clientId + ':' + secret).encode("ascii"))
                    payload = {"grant_type": "client_credentials"}
                    headers = {'Authorization': 'Bearer a2R0zfYLU_ef2pXcyBp36PgiTP5gYuCUimOnsTOjj9chMB5MpZCYzfE4zULFYknJa9edApMste6zAGjxnLhvrP2Q3EDLvQn7_DDI8qqfb0rTxo3Y3a9J4qIQf19dXnYx'}
                    key = 'fYlpdrJQZavt4FGw'
                    cityID = "9179"
                    PARAMS = {'min_date': startDate,'max_date': endDate}
                    eventsResponseDate = requests.get('https://api.songkick.com/api/3.0/metro_areas/'+ cityID+'/calendar.json?apikey='+key, PARAMS)
                    eventsForWeek = eventsResponseDate.json()
                    eventsWeek = eventsForWeek['resultsPage']['results']['event']
                    concerts =[]
                    for eachEvent in eventsWeek:
                        concertTitle = eachEvent['displayName']
                        if "(" in concertTitle:
                            index = concertTitle.index('(')
                            concertTitle = concertTitle[:index-1]
                        artist = []
                        performances = eachEvent['performance']
                        for performance in performances:
                            artist.append(performance['displayName'])
                            artistName = artist[0]

                        #spotify request to get token
                        resp = requests.post("https://accounts.spotify.com/api/token",data=payload,headers={'Authorization': "Basic %s" % auth.decode("ascii")},verify=True)
                        token = resp.json()['access_token']

                        #spotify request to get artist's image
                        URL1 = "https://api.spotify.com/v1/search?q=" + artistName.lower().replace(" ", "%20") + "&type=artist"
                        r1 = requests.get(url = URL1, headers={'Authorization': 'Bearer ' + token})
                        try:
                            data1 = r1.json()['artists']['items'][0]
                            data1['images'][0]
                        except:
                            data1 = None
                        if data1 is None:
                            continue
                        imageLink= data1['images'][0]['url']
                        City = eachEvent['location']['city']
                        Venue = eachEvent['venue']['displayName']
                        if '(' in Venue:
                            index = Venue.index('(')
                            Venue = Venue[:index-1]
                        if '-' in Venue:
                            index = Venue.index('-')
                            Venue = Venue[:index-1]
                        if ',' in Venue:
                            index = Venue.index(',')
                            Venue = Venue[:index]
                        if 'Cactus' in Venue:
                            Venue = 'Cactus Cafe'
                        if 'Austin City Limits' in Venue:
                            Venue = 'ACL Live at the Moody Theater'
                        if 'Threadgill' in Venue:
                            Venue = Venue[:10]
                        if 'Stubb' in Venue:
                            Venue = Venue[:5]
                        if 'Empire' in Venue:
                            Venue = 'Empire Control Room'
                        URL =  'https://api.yelp.com/v3/businesses/search?location=austin&term=' + Venue +'&limit=50'
                        response = requests.request('GET',URL,headers=headers,data= {})
                        try:
                            businesses = response.json()['businesses']
                        except:
                            continue
                        yelpid = 'N/A'
                        if len(businesses)!=0:
                            if Venue.lower() in businesses[0]['name'].lower():
                                yelpid = businesses[0]['id']
                            elif businesses[0]['name'].lower() in Venue.lower():
                                yelpid = businesses[0]['id']
                        VenueWebsite = eachEvent['venue']['uri']
                        if VenueWebsite is None:
                            VenueWebsite = 'N/A'
                        StartingTime = eachEvent['start']['time']
                        if StartingTime is None:
                            StartingTime = '21:00:00'
                        Date = eachEvent['start']['date']
                        try:
                            headLiner = artist[0]
                        except:
                            continue
                        if "," in headLiner:
                            index = headLiner.index(',')
                            headLiner = headLiner[:index]
                        specificConcert = Concerts(city = City,concertName = concertTitle,artists = artist,venue = Venue,venueWebsite = VenueWebsite,startingTime = StartingTime,date = Date, headliner = headLiner, imageURL = imageLink, yelpID = yelpid)
                        if yelpid !='N/A':
                            concerts.append(specificConcert)
                    return concerts
