from  django.forms import ModelForm
from .models import  BloodGroup


class RegisterBloodGroup(ModelForm):


    class Meta:

        model=BloodGroup
        fields=['blood_group','gender','status','house_name','place','street_name','phone', 'pincode']