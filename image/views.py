from django.conf import settings
from django.shortcuts import render
from django.views.generic.simple import direct_to_template
from models import State

def home(request):
    context = {
        'objects': State.objects.all(),
    }
    return render(request, 'us_states.svg.html', context)