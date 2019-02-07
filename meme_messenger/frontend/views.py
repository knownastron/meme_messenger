from django.shortcuts import render, redirect, get_object_or_404
from .models import PhoneNumber
from .forms import PhoneNumberForm
from django.utils import timezone
from django.core import validators
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'frontend/index.html')

def register(request):
    if request.method == "POST":
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.reg_date = timezone.now()
            # deletes oldest number past 3
            while PhoneNumber.objects.count() > 3:
                PhoneNumber.objects.all()[0].delete()
            post.save()
            return render(request, 'frontend/reg_success.html')
    else:
        form = PhoneNumberForm()
        return render(request, 'frontend/register.html', {'form': form} )
    return render(request, 'frontend/register.html', {'form': form} )

def unsubscribe(request):
    if request.method == "POST":
        form = PhoneNumberForm(request.POST)
        country = request.POST.__getitem__('country')
        area = request.POST.__getitem__('area')
        number = request.POST.__getitem__('phone_number')
        if form.is_valid2(country, area, number):
            return render(request, 'frontend/unsub_success.html',)
        else:
            return render(request, 'frontend/unsubscribe.html', {'error': 'Phone number is not registered', 'form': form})
    else:
        form = PhoneNumberForm()
        return render(request, 'frontend/unsubscribe.html', {'form': form})


def reg_success(request):
    return render(request, 'frontend/reg_success.html')
