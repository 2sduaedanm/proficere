# Generated by Django 2.2.14 on 2020-08-05 03:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0033_auto_20200804_2217'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='useraddress',
            unique_together={('user', 'address')},
        ),
    ]
