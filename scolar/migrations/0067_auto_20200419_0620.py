# Generated by Django 3.0.2 on 2020-04-19 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0066_auto_20200419_0544'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscription',
            name='tuteur',
        ),
        migrations.AddField(
            model_name='etudiant',
            name='tuteur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scolar.Enseignant'),
        ),
    ]
