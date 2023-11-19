from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializer import *

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemViews (generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemsSerializer

class SingleMenuItemView (generics.RetrieveUpdateAPIView, generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemsSerializer

class BookingViuewSet (viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

@api_view()
@permission_classes([IsAuthenticated])
def message (request):
    return Response({'message':'This view is protected'})