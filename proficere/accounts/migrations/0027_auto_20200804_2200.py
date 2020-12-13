# Generated by Django 2.2.14 on 2020-08-05 03:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_auto_20200804_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='phoneno',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='userphone',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='address',
            unique_together={('country', 'addressline01', 'addressline02', 'addressline03', 'city', 'state', 'postalcode')},
        ),
    ]