from django.shortcuts import render
from django.http import HttpResponse
from datetime import date as d
from datetime import time as t

# Create your views here.
def index(request):
	return render(request, "index.html")

