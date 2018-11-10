from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import *
from django.contrib.auth.decorators import login_required
# from .forms import *
from django.db import transaction


# Create your views here.
def index(request):
    return render(request,"index.html")


# @login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    print(profile)
    # profile = Profile.objects.filter(user=request.user.id)
    # images = Image.objects.filter(profile = current_user)

    return render(request,'profile.html',{'profile':profile})
