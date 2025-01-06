from django.db import models

# Notice model for storing club notices
class Notice(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


# Member model for storing information about committee members
class Member(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='members/')

    def __str__(self):
        return self.name


# GalleryImage model for storing images in the gallery
class GalleryImage(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.title


# ClubMember model for new member registrations
class ClubMember(models.Model):
    # Choices for gender, religion, and blood group
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    RELIGION_CHOICES = [
        ('Islam', 'Islam'),
        ('Hindu', 'Hindu'),
        ('Christian', 'Christian'),
        ('Other', 'Other'),
    ]

    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ]

    # Core fields for member information
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=100)
    joining_date = models.DateField()
    department = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    spouse_name = models.CharField(max_length=200, blank=True)

    # Fields with choices
    religion = models.CharField(max_length=100, choices=RELIGION_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUP_CHOICES)

    # Address fields
    permanent_address = models.TextField()
    present_address = models.TextField()

    # Contact information
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=15)
    phone_office = models.CharField(max_length=15, blank=True)
    phone_residence = models.CharField(max_length=15, blank=True)

    # Profile and signature images
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    signature_image = models.ImageField(upload_to='signatures/', blank=True, null=True)

    def __str__(self):
        return self.name
