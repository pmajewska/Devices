from django.contrib import admin
from .models import Urzadzenia, Osoba, Laboratorium

# Register your models here.

admin.site.register(Urzadzenia)
admin.site.register(Osoba)
admin.site.register(Laboratorium)
