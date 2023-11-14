from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    announcements = list(Announcement.objects.all().order_by('-date'))
    context = {
        'announcements': announcements
    }
    return render(request, 'home.html', context)