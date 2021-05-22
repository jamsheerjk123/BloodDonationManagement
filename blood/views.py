from django.shortcuts import render,redirect
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
    if request.method=="POST":
        blood_group= request.POST['blood_group']

        pincode= request.POST['pincode']
        
        street_name = request.POST.get('street_name','')



        if street_name != "":
            street=street_name.capitalize()
            result=BloodGroup.objects.filter(Q(pincode=pincode)& Q(blood_group=blood_group) & Q(street_name=street))
            return render(request,'index.html',{'result': result})
        elif pincode =='':
            return render(request,'index.html')
        
        elif type(pincode) == str and blood_group != 'none': 
            
            result=BloodGroup.objects.filter(Q(pincode=pincode) & Q(blood_group=blood_group))
            return render(request,'index.html',{'result': result})

        return render(request,'index.html')

    return render(request,'index.html')

@login_required
def bloodregister(request):

    if request.method=='POST':

        form=RegisterBloodGroup(request.POST)
        if form.is_valid():
            blood_group=form.save(commit=False)
            user=request.user
            if BloodGroup.objects.filter(user=user).exists(): 
                messages.error(request,'All Ready Registered')
                return redirect('blood:home') 

                messages.error(request,'All Ready Registered')

            blood_group.user=user
            blood_group.save()
            return redirect('blood:home')
        return redirect('blood:bloodgroup')    

    form=RegisterBloodGroup()    

    return render(request,'registerblood.html',{'form':form})

@login_required
def update_status(request):
    
    if request.method=='POST':
        status=request.POST['status']
        print(status)
        user=BloodGroup.objects.get(user=request.user)
        user.status = status
        user.save(update_fields=['status'])
        return redirect('blood:home')
    return render(request,'update.html')   