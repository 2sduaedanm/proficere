# Generated by Django 2.2.14 on 2020-07-29 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_delete_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='userphoto',
            field=models.ImageField(blank=True, default='profile1.png', null=True, upload_to='photos'),
        ),
    ]
