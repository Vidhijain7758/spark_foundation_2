from django.conf.urls import url,include

from . import views
from rest_framework import routers
from accounts.views import *




urlpatterns = [
    url(r'^Coffee/$', UserCreate, name='account-create'),
    url(r'^Coffee/(?P<id>\d+)/$', user_details, name='account-create1'),
    url(r'^Coffee/$', UserCreationView.as_view()),
]
