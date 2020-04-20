from webapp.models import Venue, Concerts
import json
import requests


venuelist = Venue.objects.all()
for venue in venuelist:
    venue.delete()
   
concertlist = Concerts.objects.all()

api_key='a2R0zfYLU_ef2pXcyBp36PgiTP5gYuCUimOnsTOjj9chMB5MpZCYzfE4zULFYknJa9edApMste6zAGjxnLhvrP2Q3EDLvQn7_DDI8qqfb0rTxo3Y3a9J4qIQf19dXnYx'
headers = {'Authorization': 'Bearer a2R0zfYLU_ef2pXcyBp36PgiTP5gYuCUimOnsTOjj9chMB5MpZCYzfE4zULFYknJa9edApMste6zAGjxnLhvrP2Q3EDLvQn7_DDI8qqfb0rTxo3Y3a9J4qIQf19dXnYx'}

venue_concert_dict = {}

for c in concertlist:
    if c.venue is not None:
    
        url = "https://api.yelp.com/v3/businesses/search?location=austin&term=" + c.venue + "&limit=50"
        #url = "https://api.yelp.com/v3/businesses/search?location=austin&term=" + concertlist[2].venue + "&limit=50"

        response = requests.request("GET", url, headers=headers, data = {})
        parsed = json.loads(response.text)
        try:
            businesses = parsed["businesses"]
        except:
            continue
        if len(businesses) != 0:
            business = businesses[0]
            id = business["id"]
            name = business["name"]
            print(name)


            if (id) in venue_concert_dict:
                listitems = venue_concert_dict[id]
                listitems.append(c.concertName)
                venue_concert_dict[id] = listitems
                #venue_concert_dict[id].append(concertlist[2].concertName)
            else:
                venue_concert_dict[id] = [c.concertName]
                #venue_concert_dict[id] = [concertlist[2].concertName]

            print(venue_concert_dict[id])           

for key in venue_concert_dict:
    venue = Venue.create(key, venue_concert_dict[key])
    print(venue)
    if venue is not None:
       venue.save()
            
