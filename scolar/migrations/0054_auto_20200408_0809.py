# Generated by Django 3.0.2 on 2020-04-08 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0053_auto_20200407_1746'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ue',
            old_name='coef',
            new_name='coefold',
        ),
    ]
