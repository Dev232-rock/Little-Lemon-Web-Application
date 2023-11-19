# little_lemon_app/views.py

from django.shortcuts import render
from .models import Lemon

def lemon_list(request):
    lemons = Lemon.objects.all()
    return render(request, 'lemon_list.html', {'lemons': lemons})
