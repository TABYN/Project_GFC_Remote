# Generated by Django 3.0.2 on 2020-02-16 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0004_auto_20200215_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultat',
            name='archive',
            field=models.BooleanField(default=True),
        ),
    ]
