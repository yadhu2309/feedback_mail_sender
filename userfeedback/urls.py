from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.feedback,name='feedback'),  
    
]