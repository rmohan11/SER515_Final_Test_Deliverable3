# Generated by Django 2.1.1 on 2018-10-15 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_remove_flightdetails_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='flightinfo',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
