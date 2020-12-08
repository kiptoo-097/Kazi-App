from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse,Http404
# Create your views here.



def index(request):
    applicant=Applicant.objects.all()
    return render(request,'index.html',locals())