from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.models import CustomUser
from .models import Main
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

#@login_required
def home(request):

    main = Main.objects.get(pk=1)

    return render(request, 'front/home.html',{'main':main})



   


