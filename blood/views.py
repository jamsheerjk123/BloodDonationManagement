from django.shortcuts import render,redirect
from .forms import RegisterBloodGroup
from django.contrib.auth.decorators import login_required
from account.views import *
from django.contrib import messages
from .models import BloodGroup
from django.db.models import Q


# Create your views here.
@login_required(login_url='account:signin')
def home(request):
    if request.method=="POST":
        blood_group= request.POST['blood_group']

        pincode= request.POST['pincode']

        street_name = request.POST.get('street_name','')

        if street_name != "":
            result=BloodGroup.objects.filter(Q(pincode=pincode)& Q(blood_group=blood_group) & Q(street_name=street_name))
            return render(request,'index.html',{'result': result})
        
        
        
        result=BloodGroup.objects.filter(Q(pincode=pincode)& Q(blood_group=blood_group))
        return render(request,'index.html',{'result': result})
    
    return render(request,'index.html')

@login_required
def bloodregister(request):

    if request.method=='POST':

        form=RegisterBloodGroup(request.POST)
        if form.is_valid():
            blood_group=form.save(commit=False)
            user=request.user
            if BloodGroup.objects.filter(user=user).exists(): 

                return redirect('blood:home') 

                messages.error(request,'All Ready Registered')

            blood_group.user=user
            blood_group.save()
            return redirect('blood:home')
        return redirect('blood:bloodgroup')    

    form=RegisterBloodGroup()    

    return render(request,'registerblood.html',{'form':form})
