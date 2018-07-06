from django.contrib import admin
from django.contrib.auth import views as auth_views

from .models import Travels_Model, Respond_Model, Photo_Model, Trip_Description_Model, Record_For_Travel_Model

class Travels_Model_Admin(admin.ModelAdmin):
	list_display = ['travel_name', 'travel_author', 'travel_route', 'travel_created_on']
	ordering = ['travel_created_on', 'travel_route']

class Respond_Model_Admin(admin.ModelAdmin):
	list_display = ['respond_author', 'respond_text', 'respond_created_on']
	ordering = ['respond_author', 'respond_created_on']

class Photo_Model_Admin(admin.ModelAdmin):
	list_display = ['photo_author', "photo_created_on", "travel_name_photo"]
	ordering = ['photo_author', "photo_created_on"]


class Trip_Model_Admin(admin.ModelAdmin):
	list_display = ['trip_organizer', 'trip_point', 'number_of_seats', 'departure_date', 'date_of_arrival', 'trip_created_on']
	ordering = ['trip_organizer', 'trip_point', 'trip_created_on']

class Record_For_Travel_Admin(admin.ModelAdmin):
	list_display = ['trip_name', 'first_name', 'last_name', 'mail']

admin.site.register (Travels_Model, Travels_Model_Admin)
admin.site.register (Respond_Model, Respond_Model_Admin)
admin.site.register (Photo_Model, Photo_Model_Admin)
admin.site.register (Trip_Description_Model, Trip_Model_Admin)
admin.site.register (Record_For_Travel_Model, Record_For_Travel_Admin)