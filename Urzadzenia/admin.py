from django.contrib import admin
from .models import Urzadzenia, Osoba, Laboratorium, Post

# Register your models here.

admin.site.register(Urzadzenia)
admin.site.register(Osoba)
admin.site.register(Laboratorium)
admin.site.register(Post)