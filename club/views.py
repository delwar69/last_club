from django.shortcuts import render
from .models import Notice, Member, GalleryImage

def home(request):
    notices = Notice.objects.all()
    members = Member.objects.all()
    gallery = GalleryImage.objects.all()
    return render(request, 'club/home.html', {'notices': notices, 'members': members, 'gallery': gallery})


# About Us Section Views
def about_club(request):
    return render(request, 'club/about_club.html')

def president(request):
    return render(request, 'club/president.html')

def secretary(request):
    return render(request, 'club/secretary.html')

def former_president(request):
    return render(request, 'club/former_president.html')

def former_secretary(request):
    return render(request, 'club/former_secretary.html')

def adhoc_committee(request):
    return render(request, 'club/adhoc_committee.html')

def all_members(request):
    return render(request, 'club/all_members.html')

# Service & Facilities Section Views
def celebration(request):
    return render(request, 'club/celebration.html')

def congratulations(request):
    return render(request, 'club/congratulations.html')

# Sports & Fitness Section Views
def badminton(request):
    return render(request, 'club/badminton.html')

def gym(request):
    return render(request, 'club/gym.html')

def table_tennis(request):
    return render(request, 'club/table_tennis.html')

def cards(request):
    return render(request, 'club/cards.html')

def squash(request):
    return render(request, 'club/squash.html')

# contact Section Views
def contact(request):
    return render(request, 'club/contact.html')

# new_member_registration Section Views
def new_member_registration(request):
    return render(request, 'club/new_member_registration.html')

# Carousel or Home View (if applicable)
#def home(request):
#    return render(request, 'club/home.html')