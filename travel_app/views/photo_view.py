# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from ..models import Photo_Model
from ..models import Travels_Model

from ..util import get_current_album

def get_tweets(tweets_topic):
	tweets = []

	import twitter
	api = twitter.Api(consumer_key='yBcRZ3dJX1CmRTw4ZmdUh7qVW',
                  consumer_secret='Vbz3fCfOo2xmwamCuyLyGgHHjFPTbeTC32iTzcpYp27NbaLHUa',
                  access_token_key='991256166046027776-ffIjtRZgk3ZzGlT1K7VAs4cKEtj7dYd',
                  access_token_secret='878LsuYe00z6cwIKztbeLZiUcm8GuxsbFKyPYLi8h9anD')

	latest = api.GetSearch(raw_query="q="+tweets_topic+"%20&result_type=recent&count=20")

	for tweet in latest:
		status = tweet.text
		tweet_date = tweet.created_at
		tweets.append({'status': status, 'date': tweet_date})

	return {'tweets': tweets}

# Додаємо фото в альбом

@login_required
def add_photo(request):
	current_album = get_current_album(request)
	travels_names = Travels_Model.objects.filter(travel_name=current_album)
	
	# фото може додати тільки автор поточного альбому
	for author in travels_names:
		if str(request.user) == author.travel_author:
		
			if request.method == 'POST':
				if request.POST.get('send_button') is not None:

					errors = {}
					data = {}

					photo_author = request.user
					data ['photo_author'] = photo_author

					photo = request.FILES.get('photo')
					if not photo:
						errors['photo'] = u'Завантажте фото!'
					else:
						data ['photo'] = photo

					travel_name_photo=current_album
					#travel_name_photo = Travels_Model.objects.get(pk=request.POST['travel_name_photo'])
					if not travel_name_photo:
						errors ['travel_name_photo'] = u'Додайте назву альбому'
					else:
						data['travel_name_photo'] = travel_name_photo


					if not errors:
						new_photo = Photo_Model(**data)
						new_photo.save()

						return HttpResponseRedirect(u'%s?status_message=Фото збережено!' %(reverse('show_photo')))

					else:
						return render(request, 'add_photo.html', {'errors': errors})

				elif request.POST.get('cancel_button') is not None:
					return HttpResponseRedirect(u'%s?status_message=Додавання фото скасоване!' %(reverse('add_photo')))

			else:
				return render (request, 'add_photo.html', {})
		else:
			return HttpResponseRedirect (u'%s?status_message=Фото може додати тільки автор даного альбому!' %(reverse('show_photo')))

# показуємо фото в альбомах
def show_photo(request):
	current_album = get_current_album(request)

	if current_album:
		photo = Photo_Model.objects.filter(travel_name_photo=current_album).order_by('photo_created_on')[::-1]
		author_photo = Travels_Model.objects.filter(travel_name=current_album)

		for entry in author_photo:
			trav_description=entry.travel_description
		
		tweets_topic = str(current_album)

	else:
		photo = Photo_Model.objects.all().order_by('photo_created_on')[::-1]

	return render (request, 'show_photo.html', {'photo': photo,
												'author_photo': author_photo,
												'trav_description': trav_description,
												'tweets': get_tweets(tweets_topic)})

