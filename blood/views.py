from django.shortcuts import render, redirect
from .forms import RegisterBloodGroup
from django.contrib.auth.decorators import login_required
from account.views import *
from django.contrib import messages
from .models import BloodGroup
from django.db.models import Q
import math

# Create your views here.


@login_required(login_url='account:signin')
def home(request):
    if request.method == "POST":
        blood_group = request.POST['blood_group']

        pincode = request.POST['pincode']

        street_name = request.POST.get('street_name', '')

        if street_name != "":
            street = street_name.capitalize()
            if BloodGroup.objects.filter(street_name=street_name).exists():

                result = BloodGroup.objects.filter(Q(pincode=pincode) & Q(
                    blood_group=blood_group) & Q(street_name=street))
                return render(request, 'index.html', {'result': result})
            m=messages.error(request,"Matching Blood Group Not Available in that Street")
            return render(request,'index.html',{'m':m})    
        elif pincode == '':
            return render(request, 'index.html')

        elif type(pincode) == str and blood_group != 'none':

            result = BloodGroup.objects.filter(
                Q(pincode=pincode) & Q(blood_group=blood_group)
                )
            if result:
                return render(request, 'index.html', {'result': result,})
            else: 
                messages.error(request,"Blood Groups not available")   
            

        return render(request, 'index.html')

    return render(request, 'index.html')


@login_required
def bloodregister(request):

    if BloodGroup.objects.filter(user=request.user).exists():
        messages.error(request, 'All Ready Registered')

    if request.method == 'POST':

        form = RegisterBloodGroup(request.POST)
        if form.is_valid():
            blood_group = form.save(commit=False)
            user = request.user
            if BloodGroup.objects.filter(user=user).exists():
                BloodGroup.objects.filter(user=user).delete()

            blood_group.user = user
            blood_group.save()
            messages.success(request,"Successfully Updated" )
            return redirect('blood:home')
        return redirect('blood:bloodgroup')

    form = RegisterBloodGroup()

    return render(request, 'registerblood.html', {'form': form})


@login_required
def update_status(request):

    if request.method == 'POST':
        status = request.POST['status']
        print(status)
        user = BloodGroup.objects.get(user=request.user)
        user.status = status
        user.save(update_fields=['status'])
        return redirect('blood:home')
    return render(request, 'update.html')
