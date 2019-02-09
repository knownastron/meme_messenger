from django.shortcuts import render, redirect, get_object_or_404
from .models import PhoneNumber
from .forms import PhoneNumberForm
from django.utils import timezone
from django.core import validators
from django.contrib import messages
from core.utils.twilio import twilioObject
# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def register(request):

    if request.method == "POST":
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            number = form.save(commit=False)
            number.reg_date = timezone.now()

            while PhoneNumber.objects.count() > 4: # deletes oldest number past 5
                PhoneNumber.objects.all()[0].delete()
            number.save()
            twilioObject().send_confirmation(number.to_string())

            return render(request, 'core/reg_success.html')

    else:
        form = PhoneNumberForm()
        return render(request, 'core/register.html', {'form': form} )
    return render(request, 'core/register.html', {'form': form} )

def unsubscribe(request):
    if request.method == "POST":
        form = PhoneNumberForm(request.POST)
        country = request.POST.__getitem__('country')
        area = request.POST.__getitem__('area')
        number = request.POST.__getitem__('phone_number')
        if form.is_valid2(country, area, number):
            return render(request, 'core/unsub_success.html',)
        else:
            return render(request, 'core/unsubscribe.html', {'error': 'Phone number is not registered', 'form': form})
    else:
        form = PhoneNumberForm()
        return render(request, 'core/unsubscribe.html', {'form': form})


def reg_success(request):
    return render(request, 'core/reg_success.html')

def unsub_success(request):
    return render(request, 'core/unsub_success.html')
