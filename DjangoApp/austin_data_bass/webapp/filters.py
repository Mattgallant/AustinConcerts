import django_filters
from .models import Artist


class ArtistFilter(django_filters.FilterSet):
	class Meta:
		model = Artist
		fields = ('popularity', 'genres')