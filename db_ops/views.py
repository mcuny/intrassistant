from django.shortcuts import render
from django.http import HttpResponse
from django.forms.models import model_to_dict
from .models import Location
from datetime import datetime
# Create your views here.

def index(request):
    return HttpResponse('Hey')

def get_locations(request):
    locations = Location.objects.all()
    output = [model_to_dict(l) for l in locations]
    now = datetime.now()
    last_update = now.strftime("%B %d, %Y - %H:%M:%S")
    return render(request, 'db_ops/index.html', {'outputs': output, 'len': len(output), 'last_update': last_update})
