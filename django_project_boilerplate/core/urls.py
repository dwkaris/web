from django.urls import  path
from . import views
from .views import *

from django.views.decorators.cache import cache_page

app_name = 'core'

urlpatterns = [ 
path('', views.item_list, name='item-list'),
path('create/', create_session),
path('access', access_session),
]
