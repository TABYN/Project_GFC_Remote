# Generated by Django 3.0.2 on 2020-09-21 06:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0123_auto_20200921_0648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisme',
            name='sigle',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^[A-Z_\\-\\&\\@\\ 0-9]+$', 'Saisir en majuscule')]),
        ),
    ]
