# from django.urls import path

from django.conf.urls import url
from . import views

app_name = 'crypto'
urlpatterns = [
    # path('', views.index, name='index'),
    url(r'^plot/$', views.plot, name='plot'),
    url(r'^coins/$', views.coins, name='coins'),
    url(r'^/$', views.home, name='home'),
]
