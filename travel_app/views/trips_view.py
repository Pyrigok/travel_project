# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

import datetime

from ..models import Trip_Description_Model
from ..models import Record_For_Travel_Model

from ..util import get_current_trip

@login_required
def add_trip(request):
	
	if request.method == 'POST':
		if request.POST.get('send_button') is not None:
			
			data = {}
			errors = {}

			trip_organizer = request.user
			data['trip_organizer'] = trip_organizer

			trip_point = request.POST.get('trip_point', '').strip()
			if not trip_point:
				errors ['trip_point'] = u'Напишіть назву подорожі'
			else:
				data['trip_point'] = trip_point

			trip_description = request.POST.get('trip_description', '').strip()
			if not trip_description:
				errors['trip_description'] = u'Додайте опис маршруту!'
			else:
				data['trip_description'] = trip_description


			departure_date = request.POST.get('departure_date', '').strip()
			if not departure_date:
				errors['departure_date'] = u'Вкажіть дату виїзду'
			else:
				dep_date = datetime.date(int(departure_date.split('-')[0]), int(departure_date.split('-')[1]), int(departure_date.split('-')[2]))

				current_date = datetime.date.today()
			
				current_difference = str(dep_date - current_date).split()[0]
			
				if (str(dep_date) == str(current_date)) or int(current_difference) > 0:
					data['departure_date'] = departure_date
				else:
					errors['departure_date'] = u'Вкажіть коректну дату!'


			date_of_arrival = request.POST.get('date_of_arrival', '').strip()
			if not date_of_arrival:
				errors['date_of_arrival'] = u'Вкажіть дату приїзду!'
			else:
				arr_date = datetime.date(int(date_of_arrival.split('-')[0]), int(date_of_arrival.split('-')[1]), int(date_of_arrival.split('-')[2]))

				date_difference = str(arr_date - dep_date).split()[0]

				if (str(arr_date) == str(dep_date)) or int(date_difference) > 0:
					data['date_of_arrival'] = date_of_arrival
					

				else:
					errors['date_of_arrival'] = u'Вкажіть коректну дату!'
				
			number_of_seats = request.POST.get('number_of_seats', '').strip()
			if not number_of_seats:
				errors['number_of_seats'] = u'Вкажіть кількість можливих місць!'
			elif number_of_seats.isdigit():
				data['number_of_seats'] = number_of_seats
			else:
				errors['number_of_seats'] = u'Введіть кількість у цифрах!'

			if not errors:
				new_trip = Trip_Description_Model(**data)
				new_trip.save()

				return HttpResponseRedirect('%s?status_message=Поїздку додано!' %(reverse('plan_trip')))

			else:
				return render(request, 'plan_trip.html', {'errors': errors})

		elif request.POST.get('cancel_button') is not None:
			return HttpResponseRedirect('%s?status_message=Скасовано' %(reverse('plan_trip')))

	else:
		
		return render(request, 'plan_trip.html', {})
		


def trips_list(request):
	trip_list = Trip_Description_Model.objects.all().order_by('trip_created_on')[::-1]
	return render(request, 'trip_list.html', {'trip_list': trip_list})
	


@login_required
def to_join_the_trip(request):
	
#	інформація про вибрану подорож
	current_trip = get_current_trip(request)
	cur_trip = Trip_Description_Model.objects.filter(trip_point=current_trip)
	
#	список записаних туристів на конкретку подорож
	tourist_list = Record_For_Travel_Model.objects.filter(trip_name=current_trip)
	number_of_tourists = len(tourist_list) # 	кількість вже записаних туристів

	# перевірка, чи ще є вільні місця
	for entry in cur_trip:
		number_of_seats = entry.number_of_seats # кількість можливих місць


#	подання заявки
	if number_of_seats > number_of_tourists:	
		free_seats = number_of_seats - number_of_tourists
		seats_info = u'%s' %(free_seats)

		if request.method == 'POST':
			if request.POST.get('send_button') is not None:

				errors = {}
				data = {}

				trip_name = current_trip
				data['trip_name'] = trip_name

				mail = request.user.email
				data['mail'] = mail

				first_name = request.POST.get('first_name', '').strip()
				if not first_name:
					errors['first_name'] = u"Вкажіть ваше ім'я!"
				else:
					data['first_name'] = first_name

				last_name = request.POST.get('last_name', '').strip()
				if not last_name:
					errors['last_name'] = u"Вкажіть ваше прізвище!"
				else:
					data['last_name'] = last_name

				if not errors:
					new_tourist = Record_For_Travel_Model(**data)
					new_tourist.save()

					return HttpResponseRedirect(u'%s?status_message=Вас записано!' %(reverse('to_join_the_trip')))

				else:
					return render(request, 'to_join_the_trip.html', {'errors': errors, 'cur_trip': cur_trip, 'seats_info': seats_info, 'tourist_list': tourist_list})


			elif request.POST.get('cancel_button') is not None:
				return HttpResponseRedirect(u'%s?status_message=Скасовано!' %(reverse('to_join_the_trip')))	

		else:
			return render (request, 'to_join_the_trip.html', {'cur_trip': cur_trip, 'seats_info': seats_info, 'tourist_list': tourist_list})

	else:
		seats_info = u'Вже немає!'
		
		return render(request, 'to_join_the_trip.html', {'cur_trip': cur_trip, 'seats_info': seats_info, 'tourist_list': tourist_list})
	