# Generated by Django 2.1.1 on 2018-10-15 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinginfo',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='customerinfo',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='flightdetails',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='flightinfo',
            options={'managed': False},
        ),
    ]
