# Generated by Django 3.0.2 on 2020-11-23 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0155_salle_capacity'),
    ]

    operations = [
        migrations.AddField(
            model_name='pv',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
