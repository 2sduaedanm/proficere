# Generated by Django 3.1.7 on 2021-03-06 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instruct', '0007_auto_20210305_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='displayorder',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='challengecurriculum',
            name='displayorder',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='challengetype',
            name='displayorder',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='curriculum',
            name='displayorder',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='progression',
            name='displayorder',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='status',
            name='displayorder',
            field=models.IntegerField(null=True),
        ),
    ]
