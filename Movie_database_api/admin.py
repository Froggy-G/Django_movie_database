from django.contrib import admin
from .models import Actor, Genre, Movie, RatingStar, Rating

# Register your models here.

admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(RatingStar)
admin.site.register(Rating)