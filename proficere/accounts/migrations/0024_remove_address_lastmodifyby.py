# Generated by Django 2.2.14 on 2020-07-29 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_auto_20200729_0213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='lastmodifyby',
        ),
    ]
