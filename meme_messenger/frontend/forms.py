from django import forms
from .models import PhoneNumber
from django.core.exceptions import ValidationError

import re

class PhoneNumberForm(forms.ModelForm):

    class Meta:
        model = PhoneNumber
        fields = ('country', 'area', 'phone_number')
        labels = {
               'country': 'Country code',
               'area': 'Area code',
               'phone_number': 'Phone number'
            }

    def clean(self):
        super().clean()
        data = self.cleaned_data
        country = data['country']
        area = data['area']
        phone_number = data['phone_number']
        if re.search('[a-zA-Z]', country) or re.search('[a-zA-Z]', area) or re.search('[a-zA-Z]', phone_number):
            raise forms.ValidationError("Input must be digits.")
        if len(country) != 1:
            raise forms.ValidationError("Country code must be 1 digit.")
        if len(area) != 3:
            raise forms.ValidationError("Area code must be 3 digits.")
        if len(phone_number) != 7:
            raise forms.ValidationError("Phone number must be 7 digits.")
        return data

    # def is_valid(self):
    #     valid = super(PhoneNumberForm, self).is_valid()
    #     if not valid:
    #         return False
    #
    #
    #     data = self.cleaned_data
    #     if re.search('[a-zA-Z]', data['country']):
    #         raise forms.ValidationError("Input must be digits.")
    #         return False
    #     if re.search('[a-zA-Z]', data['area']):
    #         raise forms.ValidationError("Input must be digits.")
    #         return False
    #     if re.search('[a-zA-Z]', data['phone_number']):
    #         raise forms.ValidationError("Input must be digits.")
    #         return False
    #     return True

    def is_valid2(self, country, area, phone_number):
        """
        Returns true if the country, area, and phone_number are in the database.
        false otherwise. Used for unsubscribing a number.
        """
        try:
            number_model = PhoneNumber.objects.get(country=country, area=area, phone_number=phone_number)
            number_model.delete()
            return True
        except:
            return False
