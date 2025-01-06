from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.templatetags.static import static
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .models import Notice, Member, GalleryImage, ClubMember
from .forms import ClubMemberForm
import os
from django.conf import settings
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
#from reportlab.pdfbase import pdfmetrics
#from reportlab.pdfbase import pdfmetrics
#from reportlab.lib import pdfmetrics
#from reportlab import pdfmetrics
#from reportlab import pdfmetrics

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

# Contact Section Views
def contact(request):
    return render(request, 'club/contact.html')

# View to handle new member registration
def new_member_registration(request):
    if request.method == 'POST':
        form = ClubMemberForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form and generate the club member object
            club_member = form.save()

            # Generate PDF
            pdf_response = generate_member_pdf(club_member)
            return pdf_response
    else:
        form = ClubMemberForm()

    return render(request, 'club/new_member_registration.html', {'form': form})

# Generate member PDF with provided details

def generate_member_pdf(club_member):
    # Create a PDF document in memory
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=registration_form_{club_member.id}.pdf'

    # Create the PDF document
    c = canvas.Canvas(response, pagesize=letter)
    c.setFont("Helvetica", 12)

    # Add the BTV Club Logo (Top left corner)
    logo_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'btvclub_logo.png')
    c.drawImage(logo_path, 40, 750, width=50, height=50)  # Positioning the logo

    # Add Titles (Bangla & English) aligned with the logo
    c.setFont("Helvetica-Bold", 14)
    c.drawString(150, 770, "বাংলাদেশ টেলিভিশন অফিসার্স ক্লাব")  # Bangla title
    c.setFont("Helvetica", 12)
    c.drawString(150, 755, "Bangladesh Television Officers' Club")  # English title

    # Add Red Shade Margin (Horizontal line across the page)
    c.setStrokeColor(colors.red)
    c.setLineWidth(4)
    c.line(0, 745, 600, 745)  # Horizontal red line

    # Positioning for profile picture (left side, standard passport size)
    y_position = 710
    profile_pic_size = 35  # Standard passport size (in mm)
    if club_member.profile_picture:
        c.drawImage(club_member.profile_picture.path, 450, y_position - profile_pic_size, width=profile_pic_size, height=45)

    # Add member details below profile picture
    y_position -= 60  # Adjust y-position to leave space for the profile picture
    line_height = 15

    details = [
        f"Membership ID: {club_member.id}",
        f"Name: {club_member.name}",
        f"Designation: {club_member.designation}",
        f"Joining Date: {club_member.joining_date}",
        f"Department: {club_member.department}",
        f"DOB: {club_member.date_of_birth}",
        f"Spouse Name: {club_member.spouse_name}",
        f"Religion: {club_member.religion}",
        f"Gender: {club_member.gender}",
        f"Permanent Address: {club_member.permanent_address}",
        f"Present Address: {club_member.present_address}",
        f"Email: {club_member.email}",
        f"Mobile: {club_member.mobile}",
        f"Phone (Office): {club_member.phone_office}",
        f"Phone (Residence): {club_member.phone_residence}",
        f"Blood Group: {club_member.blood_group}",
    ]

    for detail in details:
        c.drawString(150, y_position, detail)
        y_position -= line_height

    # Add Signature Image if available
    if club_member.signature_image:
        c.drawImage(club_member.signature_image.path, 450, y_position - 40, width=100, height=35)

    # Finalize the PDF
    c.showPage()
    c.save()

    return response