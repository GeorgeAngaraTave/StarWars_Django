from django.contrib import admin
from .models import Movie, MoviePharacter, Pharacter, Planet

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display=("id", "name", "director", "history_of", "release_date")
    search_fields=("name", "director", "history_of", "release_date")
    date_hierarchy=("release_date")
    list_filter=("release_date",)

class PharacterAdmin(admin.ModelAdmin):  
    list_display=("id", "name")   
    
    
class PlanetAdmin(admin.ModelAdmin):
    list_display=("name",)  

admin.site.register(Movie, MovieAdmin)
admin.site.register(Pharacter, PharacterAdmin)
#admin.site.register(MoviePharacter)
admin.site.register(Planet, PlanetAdmin)