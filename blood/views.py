from django.shortcuts import render,redirect
from .forms import RegisterBloodGroup
from django.contrib.auth.decorators import login_required
from account.views import *
from django.contrib import messages
from .models import BloodGroup


# Create your views here.
@login_required(login_url='account:signin')
def home(request):
    
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
