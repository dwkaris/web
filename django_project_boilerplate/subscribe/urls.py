from django.urls import  path
from . import views
from .views import *

app_name = 'subscribe'

urlpatterns = [ 
path('', views.subscribe, name = 'subscribe'),
]