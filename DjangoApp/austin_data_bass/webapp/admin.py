from django.contrib import admin
from .models import Artist
#from .models import Concert
from .models import Venue
from .models import Concerts

# Register your models here.
admin.site.register(Artist)
admin.site.register(Venue)
admin.site.register(Concerts)
