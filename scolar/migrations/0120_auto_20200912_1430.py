# Generated by Django 3.0.2 on 2020-09-12 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0119_auto_20200908_0505'),
    ]

    operations = [
        migrations.AddField(
            model_name='enseignant',
            name='otp',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='type',
            field=models.CharField(choices=[('CF', 'Contrôle Final'), ('CI', 'Contrôle Intérmédiaire'), ('INT1', 'Interrogation 1'), ('INT2', 'Interrogation 2'), ('INT3', 'Interrogation 3'), ('INT4', 'Interrogation 4'), ('TP1', 'Travail Pratique 1'), ('TP2', 'Travail Pratique 2'), ('TP3', 'Travail Pratique 3'), ('TP4', 'Travail Pratique 4'), ('PR1', 'Projet 1'), ('PR2', 'Projet 2'), ('PR3', 'Projet 3'), ('PR4', 'Projet 4'), ('CC', 'Contrôle Continu'), ('Rapporteur', 'PFE: Evaluation du rapport'), ('Jury', 'PFE: Evaluation du jury'), ('Encadreur', "PFE: Evaluation de l'encadreur"), ('Rapport', 'Master: Evaluation du rapport'), ('Soutenance', "Master: Evaluation de l'oral"), ('Poster', 'Master: Evaluation du Poster')], max_length=15),
        ),
    ]
