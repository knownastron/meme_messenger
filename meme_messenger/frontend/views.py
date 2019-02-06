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
            return redirect('reg_success')
    else:
        form = PhoneNumberForm()
        return render(request, 'frontend/register.html', {'form': form} )
    return render(request, 'frontend/register.html', {'form': form} )

def unsubscribe(request):
    if request.method == "POST":

        country = request.POST.__getitem__('country')
        area = request.POST.__getitem__('area')
        number = request.POST.__getitem__('phone_number')
        try:
            number_model = PhoneNumber.objects.get(country=country, area=area, phone_number=number)
            print(number_model)
            return redirect('reg_success')
        except:
            messages.error(request, "Error")
            return render(request, 'frontend/index.html')

    else:
        form = PhoneNumberForm()
        return render(request, 'frontend/unsubscribe.html', {'form': form})


def reg_success(request):
    return render(request, 'frontend/reg_success.html')
