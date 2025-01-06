from django import forms
from .models import ClubMember

class ClubMemberForm(forms.ModelForm):
    class Meta:
        model = ClubMember
        fields = '__all__'  # Includes all fields from the model
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter full name'}),
            'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter designation'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter department'}),
            'joining_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'spouse_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter spouse name'}),
            'religion': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'blood_group': forms.Select(attrs={'class': 'form-control'}),
            # Add more widgets as needed for other fields in the model
        }

    # Optional: Add custom validation if needed
    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if date_of_birth is None:
            raise forms.ValidationError("Date of Birth is required.")
        return date_of_birth

    def clean_joining_date(self):
        joining_date = self.cleaned_data.get('joining_date')
        if joining_date is None:
            raise forms.ValidationError("Joining Date is required.")
        return joining_date
