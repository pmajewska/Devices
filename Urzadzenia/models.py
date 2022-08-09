from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Laboratorium(models.Model):
    def __str__(self):
        return self.Numer_laboratorium
    Numer_laboratorium = models.CharField(max_length=10, default='')

    class Meta:
        verbose_name = 'Laboratorium'
        verbose_name_plural = 'Laboratoria'

class Osoba(models.Model):
    def __str__(self):
        return self.Imię_i_Nazwisko
    Imię_i_Nazwisko = models.CharField(max_length=30, default='')
    Dodatkowe_informmacja = models.TextField(blank=True, default='')
    class Meta:
        verbose_name = 'Osoba odpowiedzialna'
        verbose_name_plural = 'Osoby odpowiedzialne'


class Urzadzenia(models.Model):
    Nazwa = models.CharField(max_length=100)
    Opis = models.TextField(blank=True)
    Numer_inwentarzowy = models.CharField(max_length=30, default='')
    Numer_laboratorium = models.ForeignKey(Laboratorium, on_delete=models.CASCADE, null=True)
    Osoba_odpowiedzialna = models.ForeignKey(Osoba, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.Nazwa
    class Meta:
        verbose_name = 'Urządzenie'
        verbose_name_plural = 'Urządzenia'

class Post(models.Model):
    Nazwa = models.ForeignKey(Urzadzenia, on_delete=models.CASCADE, null=True)
    Urzytkownik = models.ForeignKey(User, on_delete=models.PROTECT)
    Czas_i_data_rozpoczęcia_pracy = models.DateTimeField(default=timezone.now)
    Czas_i_data_zakończenia_pracy = models.DateTimeField(default=timezone.now)
    Uwagi = models.TextField(blank=True)
    def __str__(self):
        return str(self.Nazwa) + ' | ' + str(self.Urzytkownik) + ' | ' + str(self.Czas_i_data_rozpoczęcia_pracy)
    
    def get_absolute_url(self):
        return reverse('post_detail', args=(str(self.id)))

    class Meta:
        verbose_name = 'Wpis urzytkownika'
        verbose_name_plural = 'Wpisy urzytkowników'

