# Generated by Django 2.2.10 on 2022-11-07 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0224_auto_20221106_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='posteriori',
            field=models.BooleanField(blank=True, default='False', verbose_name='Posteriori'),
        ),
    ]
