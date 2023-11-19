from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserSerializer (serializers.ModelSerializer):
    class ModelSerializer:
        model = User
        fields = ['ID','url', 'username', 'email', 'groups']

class BookingSerializer (serializers.ModelSerializer):
    class Meta: 
        model = Booking
        fields = '__all__'

class MenuItemsSerializer (serializers.ModelSerializer):
    class Meta: 
        model = MenuItems
        fields = '__all__'

