# Generated by Django 2.2.10 on 2022-11-29 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0235_mandat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mandat',
            name='article_mandat',
        ),
    ]
