from django import forms
from .models import PhoneNumber

class PhoneNumberForm(forms.ModelForm):

    class Meta:
        model = PhoneNumber
        fields = ('country', 'area', 'phone_number')
