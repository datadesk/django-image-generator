from django.conf import settings
from django.shortcuts import render
from models import State

def home(request):
    context = {
        'objects': State.objects.all(),
    }
    return render(request, 'us_states.svg.html', context)