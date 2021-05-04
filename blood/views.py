from django.shortcuts import render,redirect
from .forms import RegisterBloodGroup

# Create your views here.
def home(request):
    return render(request,'index.html')

def bloodregister(request):

    if request.method=='POST':

        form=RegisterBloodGroup(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blood:home')

    form=RegisterBloodGroup()    

    return render(request,'registerblood.html',{'form':form})
