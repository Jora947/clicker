from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MainCycle

# Create your views here.
def index(request):
    maincycle = MainCycle.objects.first()
    return render(request, 'index.html', {'maincycle': maincycle})

@api_view(['GET'])
def call_click(request):
    maincycle = MainCycle.objects.first()
    maincycle.click()
    maincycle.save()
    
    return Response(maincycle.coins_count)