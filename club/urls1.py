from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # About Us Section
    path('about_club/', views.about_club, name='about_club'),
    path('president/', views.president, name='president'),
    path('secretary/', views.secretary, name='secretary'),
    path('former_president/', views.former_president, name='former_president'),
    path('former_secretary/', views.former_secretary, name='former_secretary'),
    path('adhoc_committee/', views.adhoc_committee, name='adhoc_committee'),
    path('all_members/', views.all_members, name='all_members'),

    # Service & Facilities Section
    path('celebration/', views.celebration, name='celebration'),
    path('congratulations/', views.congratulations, name='congratulations'),

    # Sports & Fitness Section
    path('badminton/', views.badminton, name='badminton'),
    path('gym/', views.gym, name='gym'),
    path('table_tennis/', views.table_tennis, name='table_tennis'),
    path('cards/', views.cards, name='cards'),
    path('squash/', views.squash, name='squash'),
    
    #contact section
    path('contact/', views.contact, name='contact'),
    
    #new_members registrations section
    path('new_member_registration/', views.new_member_registration, name='new_member_registration'),
    
    # Home View
    path('', views.home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
