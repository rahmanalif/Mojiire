from django.shortcuts import render, redirect
# from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from .forms import Contact
from .forms import Mentee
from .forms import Mentor
from core.models import EventsGallery
from core.models import UpcomingEvent

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact-success')
    else:
        form = Contact()
    return render(request, "index.html", {'form': form})

def about(request):
    testing = 1

    context = {
        'testing': testing
    }
    return render(request, "about.html", context)

def contact(request):
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact-success')
    else:
        form = Contact()
    return render(request, 'contact.html', {'form': form})

def programcomponents(request):
    testing = 1

    context = {
        'testing': testing
    }
    return render(request, "program-components.html", context)

def initiatives(request):
    testing = 1

    context = {
        'testing': testing
    }
    return render(request, "initiatives.html", context)

def news(request):
    testing = EventsGallery.objects.all()
    upcoming_events = UpcomingEvent.objects.filter(is_published=True)

    context = {
        'testing': testing,
        'upcoming_events': upcoming_events
    }
    return render(request, "news.html", context)

def mentors(request):
    if request.method == 'POST':
        form = Mentor(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mentors-signup-success')
    else:
        form = Mentor()
    return render(request, 'mentors.html', {'form': form})

def mentees(request):
    if request.method == 'POST':
        form = Mentee(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mentees-signup-success')
    else:
        form = Mentee()
    return render(request, 'mentees.html', {'form': form})

def donate(request):
    testing = 1

    context = {
        'testing': testing
    }
    return render(request, "donate.html", context)

def contactsuccess(request):
    testing = 1

    context = {
        'testing': testing
    }
    return render(request, "contact-success.html", context)

def menteessignupsuccess(request):
    testing = 1

    context = {
        'testing': testing
    }
    return render(request, "mentee-signup-success.html", context)

def mentorssignupsuccess(request):
    testing = 1

    context = {
        'testing': testing
    }
    return render(request, "mentor-signup-success.html", context)
