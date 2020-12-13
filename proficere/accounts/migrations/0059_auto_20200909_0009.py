# Generated by Django 3.0.9 on 2020-09-09 05:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0058_auto_20200909_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='lastmodifyby',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Addressmodifier', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='lastmodifyby',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='UserAddressmodifier', to=settings.AUTH_USER_MODEL),
        ),
    ]