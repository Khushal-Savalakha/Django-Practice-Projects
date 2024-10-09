from django.contrib import admin
from temp.models import Movie
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    fields = ['id', 'title', 'description', 'image', 'url']  # Use 'id' instead of '_id'

admin.site.register(Movie)

# from django.contrib import admin
# from temp.models import Movie

# class MovieAdmin(admin.ModelAdmin):
#     # Display the 'id' field along with other fields
#     fields = ['id', 'title', 'description', 'image', 'url']  # Add 'id' to fields

#     # Make 'id' read-only so it is displayed but not editable
#     readonly_fields = ['id']

# admin.site.register(Movie, MovieAdmin)
