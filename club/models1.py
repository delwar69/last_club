from django.db import models

class Notice(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Member(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='members/')

    def __str__(self):
        return self.name

class GalleryImage(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.title

#forms for members models
class club_Member(models.Model):
    # Define choices for gender, religion, and blood group
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
    
    # Define the model fields
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=100)
    joining_date = models.DateField()
    department = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    spouse_name = models.CharField(max_length=200)
    
    # Fields with choices
    religion = models.CharField(max_length=100, choices=RELIGION_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUP_CHOICES)
    
    permanent_address = models.TextField()
    present_address = models.TextField()
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=15)
    phone_office = models.CharField(max_length=15, blank=True)
    phone_residence = models.CharField(max_length=15, blank=True)
    
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    signature_image = models.ImageField(upload_to='signatures/', blank=True, null=True)

    def __str__(self):
        return self.name