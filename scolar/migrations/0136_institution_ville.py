# Generated by Django 3.0.2 on 2020-10-22 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0135_institution_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='ville',
            field=models.CharField(default='', max_length=50),
        ),
    ]
