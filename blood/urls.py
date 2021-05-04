from django.urls import path
from .views import home,bloodregister

app_name='blood'

urlpatterns =[
    path('',home,name='home'),
    path('bloodregister/',bloodregister,name='bloodgroup')
]