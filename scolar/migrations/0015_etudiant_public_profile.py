# Generated by Django 3.0.2 on 2020-03-13 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0014_inscription_archive'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiant',
            name='public_profile',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
