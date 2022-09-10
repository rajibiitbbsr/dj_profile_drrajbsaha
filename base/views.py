from django.shortcuts import render
from django.views.generic.list import ListView
from .models import UserData



class HomePageView(ListView):
    model = UserData
    template_name= "base/index.html"




# Create your views here.
