# Generated by Django 4.0.6 on 2022-08-02 20:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Urzadzenia', '0002_laboratorium_osoba_alter_urzadzenia_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Czas_i_data_rozpoczęcia_pracy', models.DateTimeField()),
                ('Czas_i_data_zakończenia_pracy', models.DateTimeField()),
                ('Uwagi', models.TextField(blank=True)),
                ('Urzytkownik', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]