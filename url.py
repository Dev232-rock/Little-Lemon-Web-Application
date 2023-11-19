# little_lemon_app/urls.py

from django.urls import path
from .views import lemon_list

urlpatterns = [
    path('lemons/', lemon_list, name='lemon_list'),
]
