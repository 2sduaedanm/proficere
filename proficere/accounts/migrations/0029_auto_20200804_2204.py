# Generated by Django 2.2.14 on 2020-08-05 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_auto_20200804_2202'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='address',
            unique_together={('country', 'addressline01', 'addressline02', 'city', 'state', 'postalcode')},
        ),
    ]
