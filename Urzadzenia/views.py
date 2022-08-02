from django.shortcuts import render
from django.http import HttpResponse
from .models import Urzadzenia, Laboratorium

def index(request):
    laboratorium = Laboratorium.objects.all()
    dane = {'laboratorium': laboratorium}
    return render(request, 'szablon.html', dane)

def lab(request, id):
    lab_number = Laboratorium.objects.get(pk=id)
    lab_urzadzenie = Urzadzenia.objects.filter(Numer_laboratorium = lab_number)
    laboratorium = Laboratorium.objects.all()
    dane = {'lab_number': lab_number, 'lab_urzadzenie': lab_urzadzenie, 'laboratorium': laboratorium}
    return render(request, 'lab_urzadzenia.html', dane)

def dev(request, id):
    dev_number = Urzadzenia.objects.get(pk=id)
    laboratorium = Laboratorium.objects.all()
    dane = {'dev_number': dev_number, 'laboratorium': laboratorium}
    return render(request, 'urzadzenia.html', dane)
