from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from .forms import LandForm, HouseForm
from .models import Land, House
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import User

# Create your views here.
def home(request):
    location = request.GET.get('region', None)
    query = request.GET.get('q', None)
    property_sellrent = request.GET.get('property_sell_or_rent', None)
    house_data = House.objects.all()
    land_data = Land.objects.all()

    if query is not None:
        house_data = house_data.filter(Location__icontains = query)
    if query is not None:
        land_data = land_data.filter(Location__icontains = query)
    if location is not None:
        house_data = house_data.filter(Location__icontains = location)
    if location is not None:
        land_data = land_data.filter(Location__icontains = location)
    if property_sellrent is not None:
        house_data = house_data.filter(Type__icontains = property_sellrent)
    home_template = 'digital_property/home.html'
    myDate = datetime.now()
    context = {
        'date': myDate,
        'house_data': house_data,
        'land_data': land_data,
    }
    return render(request, home_template, context)

def about(request):
    home_template = 'digital_property/about.html'
    myDate = datetime.now()
    context = {
        'date': myDate
    }
    return render(request, home_template, context)

def contact(request):
    home_template = 'digital_property/contact.html'
    myDate = datetime.now()
    context = {
        'date': myDate
    }
    return render(request, home_template, context)

def residential_house(request):
    residential_house_queryset = House.objects.all()
    residential_house_template = 'digital_property/home_list.html'
    myDate = datetime.now()
    context = {
        'date': myDate,
        'residential_house_data': residential_house_queryset
    }
    return render(request, residential_house_template, context)

def land_list(request):
    land_queryset = Land.objects.all()
    land_template = 'digital_property/land_list.html'
    myDate = datetime.now()
    context = {
        'date': myDate,
        'lands': land_queryset
    }
    return render(request, land_template, context)

def login_page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('dashboard_home'))
    else:
        if request.method == 'POST':
            form = AuthenticationForm(data = request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request,user)
                return redirect('dashboard_home')
        else:
            form = AuthenticationForm()
    home_template = 'digital_property/login.html'
    myDate = datetime.now()
    context = {
        'date': myDate,
        'form':form
    }
    return render(request, home_template, context)

# dashboard page
@login_required(login_url = '/dashboard/authentication/user/login/')
def dashboard_home(request):
    home_template = 'digital_property/dashboard_home.html'
    myDate = datetime.now()
    context = {
        'date': myDate
    }
    return render(request, home_template, context)

@login_required(login_url = '/dashboard/authentication/user/login/')
def add_property(request):
    home_template = 'digital_property/add_property.html'
    myDate = datetime.now()
    context = {
        'date': myDate
    }
    return render(request, home_template, context)

@login_required(login_url = '/dashboard/authentication/user/login/')
def property_list(request):
    home_template = 'digital_property/property_list.html'
    myDate = datetime.now()
    context = {
        'date': myDate
    }
    return render(request, home_template, context)

def logout_page(request):
    if request.method == 'POST':
        logout(request)
        # return HttpResponseRedirect(reverse('login_page'))
        return redirect('/dashboard/authentication/user/login/')

@login_required(login_url = '/dashboard/authentication/user/login/')
def add_property_land(request):
    form = LandForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'New Land Is Added Successfully')
        return redirect('/dashboard/property/list/land/')
    home_template = 'digital_property/land.html'
    myDate = datetime.now()
    context = {
        'date': myDate,
        'form': form,
    }
    return render(request, home_template, context)

@login_required(login_url = '/dashboard/authentication/user/login/')
def add_property_house(request):
    form = HouseForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'New House Is Added Successfully')
        return redirect('/dashboard/property/list/house/')
    home_template = 'digital_property/res_home.html'
    myDate = datetime.now()
    context = {
        'date': myDate,
        'form': form,
    }
    return render(request, home_template, context)


@login_required(login_url = '/dashboard/authentication/user/login/')
def add_property_appartment(request):
    appartment_template = 'digital_property/res_appartment.html'
    myDate = datetime.now()
    context = {
        'date': myDate,
    }
    return render(request, appartment_template, context)

@login_required(login_url = '/dashboard/authentication/user/login/')
def property_list_land(request):
    home_template = 'digital_property/property_list_land.html'
    myDate = datetime.now()
    context = {
        'date': myDate,
    }
    return render(request, home_template, context)

@login_required(login_url = '/dashboard/authentication/user/login/')
def property_list_house(request):
    home_template = 'digital_property/property_list_house.html'
    myDate = datetime.now()
    context = {
        'date': myDate,
    }
    return render(request, home_template, context)
