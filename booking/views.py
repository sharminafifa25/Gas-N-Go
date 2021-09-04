from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import ContactModelForm
from .models import Contact


def contact(request):
    # form = ContactModelForm()
    # if request.method == 'POST':
    #     form = ContactModelForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('contact')
    # if request.is_ajax():
    #     form = ContactModelForm(request.POST)
    #     print(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return JsonResponse({
    #             'message': 'success'
    #         })
    return render(request, 'cat.html')  



def book(request):
    if request.method == 'POST':
        name = request.POST['name']
        fuel_type = request.POST['fuel_type']
        fuel_amount = request.POST['fuel_amount']
        password = request.POST['password']
        if fuel_type == 'petrol':
            price = int(int(fuel_amount) * 20)
        elif fuel_type == 'octane':  
            price = int(int(fuel_amount) * 20)
        elif fuel_type == 'diesel':
            price = int(int(fuel_amount) * 20) 
        elif fuel_type == 'natural_gas': 
            price = int(int(fuel_amount) * 20)
        else:
            price = int(int(fuel_amount) * 20)   


        book = Contact.objects.create(name=name, password=password, fuel_type=fuel_type, fuel_amount=fuel_amount, price=price)
        book.save()
        return redirect('book')
    else:
        return render(request, 'cat.html')