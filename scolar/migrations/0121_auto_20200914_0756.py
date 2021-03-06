# Generated by Django 3.0.2 on 2020-09-14 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0120_auto_20200912_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='type',
            field=models.CharField(choices=[('CF', 'Contrôle Final'), ('CI', 'Contrôle Intérmédiaire'), ('INT', 'Interrogation'), ('TP', 'Travail Pratique'), ('CC', 'Contrôle Continu'), ('Rapporteur', 'PFE: Evaluation du rapport'), ('Jury', 'PFE: Evaluation du jury'), ('Encadreur', "PFE: Evaluation de l'encadreur"), ('Rapport', 'Master: Evaluation du rapport'), ('Soutenance', "Master: Evaluation de l'oral"), ('Poster', 'Master: Evaluation du Poster')], max_length=15),
        ),
    ]
