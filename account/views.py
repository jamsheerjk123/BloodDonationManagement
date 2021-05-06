from django.shortcuts import render,redirect,HttpResponse
from .forms import RegisterForm
from django.contrib import messages 
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.decorators import login_required
from blood.views import home

# Create your views here.
def signup(request):
    
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if  form.is_valid():
            form.save()
            messages.success(request,'Successfully Account Created')
            return redirect('account:signin')
        return redirect('account:signup')
    else:
        form=RegisterForm()
    context ={'form':form,}
    return render (request, 'registration.html',context)



def signin(request,**kwargs):
    if request.user.is_authenticated:
        return redirect('blood:home')
    
    if request.method=='POST':

        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(email=email,password=password)
        if user:
            

            login(request,user)
            return redirect('blood:home')

        messages.error(request,'Incorrect Email or Password')
        return render(request,'login.html')  
         
    return render (request,'login.html')    

@login_required
def signout(request):
    logout(request)
    return redirect('account:signin')    