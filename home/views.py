from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request ,'home.html')

def payment(request):
    return render(request ,'payment.html')
    