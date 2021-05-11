from django.urls import path
from .views import home,bloodregister,update_status

app_name='blood'

urlpatterns =[
    path('',home,name='home'),
    path('bloodregister/',bloodregister,name='bloodgroup'),
    path('updatestatus/',update_status,name='update')
]