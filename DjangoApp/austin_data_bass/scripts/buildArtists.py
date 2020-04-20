from webapp.models import Artist, Concerts

artistlist = Artist.objects.all()
for artist in artistlist:
    artist.delete()
    
concertlist = Concerts.objects.all()
for c in concertlist:
    artist = Artist.create(c.artists[0], c.concertName)
    if artist is not None:
        try:
            artist.save()
        except:
            continue
        
