from django.shortcuts import render
from django.http import HttpResponse
from .models import Urzadzenia, Laboratorium

def index(request):
    wszystko = Laboratorium.objects.all()
    dane = {'wszystko': wszystko}
    return render(request, 'szablon.html', dane)

def lab(request, id):
    lab_number = Laboratorium.objects.get(pk=id)
    return HttpResponse(lab_number.Numer_laboratorium)
