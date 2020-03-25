from django.db import models
import requests
#from djongo import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=25)
    spotifyID = models.CharField(max_length=30)
    imageLink = models.CharField(max_length=50)
    bio = models.CharField(max_length=500)
    genres = models.CharField(max_length=50) #will be a json list of genres
    popularity = models.IntegerField()
    followers = models.IntegerField()
    topTracks = models.CharField(max_length=50) #will be a json list of tracks with their corresponding popularity
    
    def create(artistName):
        token = "BQAzTEpizT9X6bhV_VaxbnNmbbucjlArynIHPg1ln72Z_Q5LN-MCu7IgRdMYkffIK0SO2tKDAgcrnvniQSh6-qT6eZ0auaP8QalaytCilM5Z5k8eRM6gXXXzZd3rcfYI0TuCqimDmbE3eSdaYDqUUzc_Mf0dlsE"
        
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
                     imageLink = artist['bio'],
                     genres = artist['genres'],
                     popularity = artist['popularity'],
                     followers = artist['followers'],
                     topTracks = artist['topTracks'])