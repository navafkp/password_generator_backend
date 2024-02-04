from django.urls import path
from .views import save_password,get_password
urlpatterns = [
    path('api/savepassword/', save_password, name='save_password'),
    
    path('getpassword/', get_password, name='get_password')
]

