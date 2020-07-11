# Generated by Django 2.2.14 on 2020-07-08 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_emailaddress_emailtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='securityanswer01',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='securityquestion01',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.SecurityQuestion'),
        ),
    ]