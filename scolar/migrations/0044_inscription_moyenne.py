# Generated by Django 3.0.2 on 2020-04-03 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0043_auto_20200403_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscription',
            name='moyenne',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]
