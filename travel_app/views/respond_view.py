# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


from ..models import Respond_Model

# додаємо відгуки на стор. "Додати щось своє"
@login_required
def add_respond(request):
	respond = Respond_Model.objects.all()

	if request.method == 'POST':

		 # отримати дані, що прийшли в тілі методу POST форми із браузера
		if request.POST.get('send_button') is not None:

			errors = {}
			data = {}

			respond_author = request.user
			data ['respond_author'] = respond_author

			respond_text = request.POST.get('respond_text', '').strip()
			if not respond_text:
				errors ['respond_text'] = 'Коментар без добрих слів не відправляється'
			else:
				data ['respond_text'] = respond_text

		
			if not errors:
				# записати дані із словника data у модень б. д.
				respond = Respond_Model(**data)
				respond.save()

				return HttpResponseRedirect('%s?status_message=Дякуємо за коментар!' %(reverse('add_respond')))

			else:
				return render (request, 'add_respond.html', {'errors': errors})

		elif request.POST.get('cancel_button') is not None:
			return HttpResponseRedirect ('%s?status_message=Скасовано' %(reverse('add_respond')))

	else:
		return render (request, 'add_respond.html', {})



# показуємо відгуки на гол. сторінці
# функ. показу відгуків у home_view.py