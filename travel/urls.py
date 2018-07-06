# -*- coding: utf-8 -*-
from django.conf.urls import include, url, patterns
from django.contrib import admin

from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView, TemplateView

from django.contrib.auth.decorators import login_required



from .settings import MEDIA_ROOT, DEBUG

urlpatterns = [
    # Examples:
    # url(r'^$', 'travel.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # user urls
    url(r'^$', 'travel_app.views.home_view.home', name='home'),
    url(r'^respond/id', 'travel_app.views.home_view.home', name='respond'),
    url(r'^add_photo', 'travel_app.views.photo_view.add_photo', name='add_photo'),
    #url(r'^show_photo', 'travel_app.views.photo_view.show_photo', name='show_photo'),
    url(r'^add_travel', 'travel_app.views.travels_view.add_travel', name='add_travel'),
    url(r'^add_respond', 'travel_app.views.respond_view.add_respond', name='add_respond'),

    url(r'^trip_list', 'travel_app.views.trips_view.trips_list', name='trips_list'),
    url(r'^plan_trip', 'travel_app.views.trips_view.add_trip', name='plan_trip'),
    url(r'^to_join_the_trip', 'travel_app.views.trips_view.to_join_the_trip', name='to_join_the_trip'),


    url(r'^users/profile/$', login_required(TemplateView.as_view(template_name='registration/profile.html')), name='profile'),


    url(r'^album', 'travel_app.views.photo_view.show_photo', name='show_photo'),

    # registration urls
    url(r'^users/logout/$', auth_views.logout, kwargs={'next_page': 'home'}, name='auth_logout'),
    url(r'^register/complete/$', RedirectView.as_view(pattern_name="home"), name ="registration_complete"),

    # підключ. усі шаблони з django-registration
    url(r'^users/', include('registration.backends.simple.urls')),

    # social login
    url('^social/', include('social.apps.django_app.urls', namespace='social')),

    # admin urls
    url(r'^admin/', include(admin.site.urls)),
]

# Показує фото з папки медіа
if DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': MEDIA_ROOT}))