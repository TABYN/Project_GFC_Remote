# Generated by Django 3.0.2 on 2020-06-09 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0076_inscriptionperiode_periodepgm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programme',
            name='specialite',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scolar.Specialite'),
        ),
    ]
