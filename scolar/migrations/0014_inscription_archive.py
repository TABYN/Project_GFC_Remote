# Generated by Django 3.0.2 on 2020-03-07 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0013_auto_20200229_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscription',
            name='archive',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
