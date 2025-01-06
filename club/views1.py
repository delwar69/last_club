from django.shortcuts import render
from .models import Notice, Member, GalleryImage
from django.shortcuts import render, redirect
from .forms import MemberRegistrationForm
from .models import Member
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas


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
#def new_member_registration(request):
 #   return render(request, 'club/new_member_registration.html')

# View to handle new member registration
def new_member_registration(request):
    if request.method == 'POST':
        form = MemberRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form and generate the member object
            club_member = form.save()

            # Generate PDF
            pdf_response = generate_member_pdf(club_member)
            return pdf_response
    else:
        form = MemberRegistrationForm()

    return render(request, 'club/new_member_registration.html', {'form': form})

#generate member object from member registration form   data and   pdf response
def generate_member_pdf(club_member):
    # Create a PDF document in memory
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=registration_form_{club_member.membership_number}.pdf'

    # Create the PDF document
    c = canvas.Canvas(response, pagesize=letter)
    c.setFont("Helvetica", 12)

    # Add the BTV Logo to the top-left corner
    logo_path = static('images/btvclub_logo.png')
    c.drawImage(logo_path, 30, 750, width=100, height=100)

    # Add member information to the PDF
    c.drawString(200, 780, f'Membership No: {club_member.membership_number}')
    c.drawString(200, 765, f'Name: {club_member.name}')
    c.drawString(200, 750, f'Designation: {club_member.designation}')
    c.drawString(200, 735, f'Joining Date: {club_member.joining_date}')
    c.drawString(200, 720, f'Department: {club_member.department}')
    c.drawString(200, 705, f'DOB: {club_member.date_of_birth}')
    c.drawString(200, 690, f'Spouse: {club_member.spouse_name}')
    c.drawString(200, 675, f'Religion: {club_member.religion}')
    c.drawString(200, 660, f'Gender: {club_member.gender}')
    c.drawString(200, 645, f'Permanent Address: {club_member.permanent_address}')
    c.drawString(200, 630, f'Present Address: {club_member.present_address}')
    c.drawString(200, 615, f'Email: {club_member.email}')
    c.drawString(200, 600, f'Mobile: {club_member.mobile}')
    c.drawString(200, 585, f'Phone (Office): {club_member.phone_office}')
    c.drawString(200, 570, f'Phone (Residence): {club_member.phone_residence}')
    c.drawString(200, 555, f'Blood Group: {club_member.blood_group}')

    # Add Profile Picture
    c.drawImage(club_member.profile_picture.path, 30, 600, width=50, height=50)

    # Add Signature Image
    c.drawImage(club_member.signature_image.path, 30, 500, width=100, height=50)

    # Save the PDF document
    c.showPage()
    c.save()

    return response

# Carousel or Home View (if applicable)
#def home(request):
#    return render(request, 'club/home.html')