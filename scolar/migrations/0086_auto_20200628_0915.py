# Generated by Django 3.0.2 on 2020-06-28 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0085_auto_20200628_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pfe',
            name='promoteur',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
