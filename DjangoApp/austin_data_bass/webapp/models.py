from django.db import models
import requests
import base64
import six
import json

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=25)
    spotifyID = models.CharField(max_length=50)
    imageLink = models.CharField(max_length=200)
    bio = models.CharField(max_length=500)
    genres = models.CharField(max_length=150) #will be a json list of genres
    popularity = models.IntegerField()
    followers = models.IntegerField()
    topTracks = models.CharField(max_length=150) #will be a json list of tracks with their corresponding popularity
    
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
            topTracks.append({track['name'], track['popularity']})

        artist['topTracks'] = topTracks
        
        return Artist(name = artist['name'],
                     spotifyID = artist['spotifyID'],
                     imageLink = artist['imageLink'],
                     genres = artist['genres'],
                     popularity = artist['popularity'],
                     followers = artist['followers'],
                     topTracks = artist['topTracks'])



"""class Venue(models.Model):
    name = models.CharField(max_length=100)
    yelpID =  models.CharField(max_length=25)
    imageURL = models.CharField(max_length=100)
    yelpURL = models.CharField(max_length=100)
    phone = models.CharField(max_length=15) 
    reviewCount = models.IntegerField()
    rating = models.DecimalField()
    location = models.CharField(max_length=150) 
    price = models.CharField(max_length=4)

    def create(venueID):
        api_key='a2R0zfYLU_ef2pXcyBp36PgiTP5gYuCUimOnsTOjj9chMB5MpZCYzfE4zULFYknJa9edApMste6zAGjxnLhvrP2Q3EDLvQn7_DDI8qqfb0rTxo3Y3a9J4qIQf19dXnYx'
        headers = {'Authorization': 'Bearer a2R0zfYLU_ef2pXcyBp36PgiTP5gYuCUimOnsTOjj9chMB5MpZCYzfE4zULFYknJa9edApMste6zAGjxnLhvrP2Q3EDLvQn7_DDI8qqfb0rTxo3Y3a9J4qIQf19dXnYx'
        payload = {}
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
        
        venue = {
            "name": data1["name"],
            "yelpID": data1["id"],
            "imageURL": data1["image_url"],
            "yelpURL": data1["url"],
            "phone": data1["display_phone"],
            "reviewCount": data1["review_count"],
            "rating": data1["rating"],
            "location": " ".join(data1["location"]["display_address"]),
            if ("price" in data1):
                "price": data1["price"]
            else
                "price": "$$"
        }


        return Venue(name = venue['name'],
                    yelpID =  venue['yelpID'],
                    imageURL = venue['imageURL'],
                    yelpURL = venue['yelpURL'],
                    phone = venue['phone'],
                    reviewCount = venue['reviewCount'],
                    rating = venue['rating'],
                    location = venue['location'],
                    price = venue['price'])"""

    
        