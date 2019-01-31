from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
from django.http import HttpResponse
from django.http import Http404

def index(request):
   return render(request, 'index.html')
