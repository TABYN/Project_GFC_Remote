# Generated by Django 2.2.10 on 2021-11-17 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0183_auto_20211115_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='immobilier',
            name='date_facture',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='immobilier',
            name='duree_garantie',
            field=models.IntegerField(null=True),
        ),
    ]
