from django.shortcuts import render_to_response
from django.template import RequestContext

from ..models import Travels_Model
from ..models import Respond_Model

	# 	на гол. сторінці показуємо альбоми і відгуки
def home (request):

		# Спочатку останній доданий відгук
	responds = Respond_Model.objects.order_by('respond_created_on')[::-1]
	respond_count = 0

	if responds:
		for entry in responds:
			respond_count+=1

			if len(str(respond_count)) == 1:

				if respond_count == 1:
					respond = 'коментар'
				elif respond_count in range(2, 5):
					respond = 'коментарі'
				else:
					respond = 'коментарів'

			elif len(str(respond_count)) > 1:

				last_digit = int((str(respond_count))[-1])
				last_2_digits = int(str(respond_count)[-2:])
				second_digit_from_end = int(str(respond_count)[-2])
				if last_digit == 0 or last_digit in range(5, 10) or (last_2_digits in range(10, 20)):
					respond = 'коментарів'
				elif last_digit in range (2, 5):
					respond = 'коментаря'
				elif last_digit == 1 and second_digit_from_end != 1:
					respond = 'коментар'
	#якщо відгуків немає
	else:
		respond = 'коментарів'

	context = {'responds': responds, 'respond_count': respond_count, 'respond': respond}
	return render_to_response('home.html', context, context_instance=RequestContext(request))