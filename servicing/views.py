from django.shortcuts import render,HttpResponse
from .models import Car,Service
# Create your views here.

def home(request):
    return HttpResponse("Home")


def deleteredunentdata(request):
    services = Service.objects.all()
    car = Car.objects.all()
    serviceavailable = []
    for service in services:
        if service.name  in serviceavailable:
            a=Service.objects.filter(name=service).last()
            a.delete()
        else:
            # print(service.name)
           
            serviceavailable.append(service.name)
        # print(serviceavailable)
    cardata= []
    for cars in car:
        if cars in cardata:
            print(True)
            # a=Car.objects.filter(cars).last()
            # a.delete()
            print(f"Car deleted {cars.car_model}")
        else:
            cardata.append(cars)
            print(f"Car add {cars.car_model}")
        

    print(cardata)
    return HttpResponse("Deleted")