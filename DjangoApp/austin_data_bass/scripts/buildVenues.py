from webapp.models import Venue, Concerts
import json
import requests


venuelist = Venue.objects.all()
for venue in venuelist:
    venue.delete()
   
concertlist = Concerts.objects.all()

api_key='a2R0zfYLU_ef2pXcyBp36PgiTP5gYuCUimOnsTOjj9chMB5MpZCYzfE4zULFYknJa9edApMste6zAGjxnLhvrP2Q3EDLvQn7_DDI8qqfb0rTxo3Y3a9J4qIQf19dXnYx'
headers = {'Authorization': 'Bearer a2R0zfYLU_ef2pXcyBp36PgiTP5gYuCUimOnsTOjj9chMB5MpZCYzfE4zULFYknJa9edApMste6zAGjxnLhvrP2Q3EDLvQn7_DDI8qqfb0rTxo3Y3a9J4qIQf19dXnYx'}


for c in concertlist:
    url = "https://api.yelp.com/v3/businesses/search?location=austin&term=" + c.venue + "&limit=50"
    response = requests.request("GET", url, headers=headers, data = {})
    parsed = json.loads(response.text)
    businesses = parsed["businesses"]
    if len(businesses) != 0:
        business = businesses[0]
        id = business["id"]
        print(business["name"])
        venue = Venue.create(business["id"], c.concertName)

        if venue is not None:
            venue.save()
        
