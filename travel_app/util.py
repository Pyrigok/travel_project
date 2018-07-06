# функ. визначення поточно обраного альбому
def get_current_album(request):
	# обраний альбом зберіг. у cookie
	pk = request.COOKIES.get('current_album')

	if pk:
		from .models import Travels_Model
		try:
			album = Travels_Model.objects.get(pk=int(pk))
		except Travels_Model.DoesNotExist:
			return None
		else:
			return album
	else:
		return None

def get_albums(request):
	# повертає список існуючих альбомів
	from .models import Travels_Model

	current_album=get_current_album(request)

	albums = []
	for album in Travels_Model.objects.all().order_by('travel_name'):
		albums.append({
			'id': album.id,
			'author': album.travel_author,
			'title': album.travel_name,
			'cover_url': album.travel_cover.url,
			'date': album.travel_created_on,
			'selected': current_album and current_album.id == album.id and True or False
			})

	return albums

#визначення поточної подорожі
def get_current_trip(request):
	pk = request.COOKIES.get('current_trip')

	if pk:
		from .models import Trip_Description_Model
		try:
			trip = Trip_Description_Model.objects.get(pk=int(pk))

		except Trip_Description_Model.DoesNotExist:
			return None
		else:
			return trip

	else:
		return None

def get_trips(request):
	from .models import Trip_Description_Model

	current_trip = get_current_trip(request)

	trips = []
	for trip in Trip_Description_Model.objects.all().order_by('trip_point'):
		trips.append({
			'id': trip.id,
			'organizer': trip.trip_organizer,
			'point': trip.trip_point,
			'description': trip.trip_description,
			'amount': trip.number_of_seats,
			'there': trip.departure_date,
			'back': trip.date_of_arrival,
			'created_on': trip.trip_created_on
			})
	return trips
