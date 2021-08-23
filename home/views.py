from django.shortcuts import render
from .models import *
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request ,'home.html')

def payment(request):
    return render(request ,'payment.html')

def api_gas(request):
    gas_objs = Gas.objects.all()

    payload = []
    for gas_obj in gas_objs:
        result = {}
        result['pump_name'] = gas_objs.pump_name
        result['pump_image'] = gas_objs.pump_image
        result['pump_address'] = gas_objs.pump_address  
        result['available_amount'] = gas_objs.available_amount
        payload.append(result)
    return JsonResponse(payload , safe=False)    
        