# Generated by Django 2.2.10 on 2022-11-10 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0227_auto_20221110_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='engagement',
            name='type',
            field=models.CharField(choices=[('01', 'Prise en charge'), ('02', 'Depence'), ('03', 'Economie')], max_length=2, null=True),
        ),
    ]
