# Generated by Django 2.2.14 on 2020-08-05 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0032_auto_20200804_2214'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='useraddress',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='useraddress',
            constraint=models.UniqueConstraint(fields=('user', 'address'), name='unique_useraddress'),
        ),
        migrations.AddConstraint(
            model_name='useraddress',
            constraint=models.UniqueConstraint(fields=('user', 'primaryuseraddress'), name='unique_userprimary'),
        ),
    ]
