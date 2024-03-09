from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import ReservationForm


def main(request):
    template = loader.get_template('mainpage.html')
    return HttpResponse(template.render())


def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())


def our_fleet(request):
    template1 = loader.get_template('our_fleet.html')
    return HttpResponse(template1.render())


#içerisinde form oluşturuldu
def contact(request):
    form = ReservationForm()
    return render(request, 'contact.html', {'form':form})


def deneme(request):
    template = loader.get_template('deneme.html')
    return HttpResponse(template.render())
