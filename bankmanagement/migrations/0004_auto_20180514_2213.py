# Generated by Django 2.0.4 on 2018-05-14 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankmanagement', '0003_auto_20180513_1728'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Withdrawl',
            new_name='Transaction',
        ),
    ]
