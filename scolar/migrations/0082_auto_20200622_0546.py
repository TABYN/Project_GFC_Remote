# Generated by Django 3.0.2 on 2020-06-22 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0081_auto_20200621_0607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pfe',
            name='encadreur',
        ),
        migrations.AddField(
            model_name='pfe',
            name='encadrant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scolar.Enseignant'),
        ),
    ]
