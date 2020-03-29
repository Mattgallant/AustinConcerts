import requests
import json


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
    concertName = eachEvent['displayName']
    artists = []
    performances = eachEvent['performance']
    for performance in performances:
            artists.append(performance['displayName'])
    city = eachEvent['location']['city']
    venue = eachEvent['venue']['displayName']
    venueWebsite = eachEvent['venue']['uri']
    startingTime = eachEvent['start']['time']
    date = eachEvent['start']['date']
    specificConcert = {'concertName':concertName,'artists':artists,'city':city,'venue':venue,'venueWebsite':venueWebsite,'startingTime':startingTime,'date':date}
    concerts.append(specificConcert)

print(concerts[1])
