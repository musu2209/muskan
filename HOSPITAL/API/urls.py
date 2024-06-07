from django.urls import path
from . import views
urlpatterns = [    
    path('getPATIENT/', views.getPATIENT.as_view()),
    path('getMEDICINE/',views.getMEDICINE.as_view()),
    path('CreatePATIENT/',views.CreatePATIENT.as_view()),
    path('updateAddressPatient/',views.updateAddressPatient.as_view())
]   