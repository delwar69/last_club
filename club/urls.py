from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # About Us Section
    path('about_club/', views.about_club, name='about_club'),  # Overview of the club
    path('president/', views.president, name='president'),  # President details
    path('secretary/', views.secretary, name='secretary'),  # Secretary details
    path('former_president/', views.former_president, name='former_president'),  # Former presidents
    path('former_secretary/', views.former_secretary, name='former_secretary'),  # Former secretaries
    path('adhoc_committee/', views.adhoc_committee, name='adhoc_committee'),  # Ad-hoc committee details
    path('all_members/', views.all_members, name='all_members'),  # List of all members

    # Service & Facilities Section
    path('celebration/', views.celebration, name='celebration'),  # Celebrations information
    path('congratulations/', views.congratulations, name='congratulations'),  # Achievements/congratulations

    # Sports & Fitness Section
    path('badminton/', views.badminton, name='badminton'),  # Badminton details
    path('gym/', views.gym, name='gym'),  # Gym details
    path('table_tennis/', views.table_tennis, name='table_tennis'),  # Table tennis information
    path('cards/', views.cards, name='cards'),  # Card games section
    path('squash/', views.squash, name='squash'),  # Squash details

    # Contact Section
    path('contact/', views.contact, name='contact'),  # Contact details

    # New Member Registration Section
    path('new_member_registration/', views.new_member_registration, name='new_member_registration'),  # Form for new registrations

    # Home View
    path('', views.home, name='home'),  # Home page
]

# Static and Media Files in Development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
