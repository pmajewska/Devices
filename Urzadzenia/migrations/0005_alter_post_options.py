# Generated by Django 4.0.6 on 2022-08-05 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Urzadzenia', '0004_post_nazwa'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Wpis urzytkownika', 'verbose_name_plural': 'Wpisy urzytkowników'},
        ),
    ]
