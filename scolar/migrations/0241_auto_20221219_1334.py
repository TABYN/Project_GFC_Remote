# Generated by Django 2.2.10 on 2022-12-19 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0240_auto_20221213_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engagement',
            name='type',
            field=models.CharField(choices=[('Prise en charge', 'Prise en charge'), ('Depence', 'Depence')], default='', max_length=15, null=True),
        ),
    ]
