from django.db import models
from account.models import UserAccount
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class BloodGroup(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    
    check_status=(('A','Available'),('NA','Not Available'))

    Group=(('A+','A+'), ('A-' ,'A-'),('B+', 'B+'), ('B-','B-'), ('O+','O+'), ('O-','O-'), ('AB+','AB+'), ('AB-','AB-'))


    user=models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    gender=models.CharField(max_length=6,choices=GENDER_CHOICES,null=False,blank=False)
    status=models.CharField(max_length=13,choices=check_status,null=False,blank=False)
    blood_group=models.CharField(max_length=3,choices=Group,verbose_name='Blood Group',null=False,blank=False)
    house_name=models.CharField(max_length=50,verbose_name='House Name',null=False,blank=False)
    place=models.CharField(max_length=100,null=False,blank=False)
    street_name=models.CharField(max_length=100,verbose_name="street name",null=False,blank=False)
    phone= PhoneNumberField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.full_name