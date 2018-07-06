# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from ..models import Travels_Model

# додаємо подорож на сторінці "Додати щось своє"
@login_required
def add_travel(request):
	
	if request.method == 'POST':
		if request.POST.get ('send_button') is not None:

			errors = {}
			data = {}

			data ['travel_route'] = request.POST.get('travel_route', '').strip()

			# Фото автора альбому
			author_photo = request.FILES.get ('author_photo')
			if author_photo:
				data ['author_photo'] = author_photo
			else:
				return HttpResponseRedirect(u'%s?status_message=Додайте фото автора!' %(reverse('add_travel')))


			travel_author = request.user
			data ['travel_author'] = travel_author

			travel_name = request.POST.get('travel_name', '').strip()
			if not travel_name:
				return HttpResponseRedirect(u'%s?status_message=Додайте назву до вашої подорожі!' %(reverse('add_travel')))

#				errors['travel_name'] = u'Додайте назву до вашої подорожі!'
			else:
				data['travel_name'] = travel_name

			travel_cover = request.FILES.get( 'travel_cover')
			if not travel_cover:
				return HttpResponseRedirect(u'%s?status_message=Додайте обкладинку до альбому!' %(reverse('add_travel')))

#				errors['travel_cover']=u'Додайте обкладинку до альбому!'
			else:
				data ['travel_cover'] = travel_cover

			travel_description = request.POST.get('travel_description', '').strip()
			if not travel_description:
				return HttpResponseRedirect(u'%s?status_message=Додайте опис до подорожі!' %(reverse(add_travel)))
			else:
				data['travel_description'] = travel_description

			if not errors:
				travel=Travels_Model(**data)
				travel.save()

				return HttpResponseRedirect(u'%s?status_message=Створено новий альбом!' %(reverse('add_travel')))

			else:
				return render (request, 'add_travel.html', {'errors': errors})

		elif request.POST.get('cancel_button') is not None:
			return HttpResponseRedirect(u'%s?status_message=Скасовано!' %(reverse('add_travel')))

	else:
		return render (request, 'add_travel.html', {})


# показуємо обкладинки альбомів на гол. сторінці
# функ. показу альбомів у home_view.py