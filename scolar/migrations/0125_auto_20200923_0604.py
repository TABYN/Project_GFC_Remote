# Generated by Django 3.0.2 on 2020-09-23 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0124_auto_20200921_0650'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='validation',
            name='pfe-expert',
        ),
        migrations.AddConstraint(
            model_name='validation',
            constraint=models.UniqueConstraint(fields=('pfe', 'expert', 'avis'), name='pfe-expert-avis'),
        ),
    ]
