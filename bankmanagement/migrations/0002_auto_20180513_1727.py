# Generated by Django 2.0.4 on 2018-05-13 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankmanagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='role',
            field=models.CharField(max_length=15),
        ),
    ]
