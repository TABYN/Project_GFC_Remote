# Generated by Django 3.0.2 on 2020-02-28 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0010_programme_ordre'),
    ]

    operations = [
        migrations.AddField(
            model_name='activite',
            name='repeter_chaque_semaine',
            field=models.BooleanField(default=True),
        ),
        migrations.AddConstraint(
            model_name='charge',
            constraint=models.UniqueConstraint(fields=('activite', 'realisee_par'), name='activite-enseignant'),
        ),
        migrations.AddConstraint(
            model_name='periodeannee',
            constraint=models.UniqueConstraint(fields=('annee_univ', 'periode'), name='periode-annee_univ'),
        ),
        migrations.AddConstraint(
            model_name='periodeprogramme',
            constraint=models.UniqueConstraint(fields=('programme', 'periode'), name='periode-programme'),
        ),
    ]
