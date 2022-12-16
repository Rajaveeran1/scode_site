from django.shortcuts import render
from django.http import HttpResponse
from datetime import date as d
from datetime import time as t

# Create your views here.
def index(request):
	start=d(2021,2,2)
	end=d.today()
	result=start - end
	myhours=result*24

	return render(request, "index.html",{'myhours':myhours})

