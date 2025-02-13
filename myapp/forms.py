import CV
from django import forms
from .models import Contact

class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ['name', 'email', 'profile_picture']
