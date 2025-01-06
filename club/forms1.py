from django import forms
from .models import club_Member

class MemberRegistrationForm(forms.ModelForm):
    class Meta:
        model = club_Member
        fields = ['name', 'designation', 'joining_date', 'department', 'date_of_birth', 'spouse_name', 
                  'religion', 'gender', 'blood_group', 'permanent_address', 'present_address', 'email', 
                  'mobile', 'phone_office', 'phone_residence', 'profile_picture', 'signature_image']
        widgets = {
            'joining_date': forms.DateInput(attrs={'type': 'date'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

