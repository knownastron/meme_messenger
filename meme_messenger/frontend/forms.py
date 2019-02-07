from django import forms
from .models import PhoneNumber

class PhoneNumberForm(forms.ModelForm):

    class Meta:
        model = PhoneNumber
        fields = ('country', 'area', 'phone_number')

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
