from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'position_applied', 'experience', 'application_status']
        widgets = {
            'application_status': forms.Select(choices=JobApplication.STATUS_CHOICES),
        }
