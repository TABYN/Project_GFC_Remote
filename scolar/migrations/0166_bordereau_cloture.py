# Generated by Django 3.1.7 on 2021-05-02 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0165_auto_20210429_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='bordereau',
            name='cloture',
            field=models.BooleanField(default=False),
        ),
    ]
