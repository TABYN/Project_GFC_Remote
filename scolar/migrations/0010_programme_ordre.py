# Generated by Django 3.0.2 on 2020-02-21 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0009_auto_20200220_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='programme',
            name='ordre',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
