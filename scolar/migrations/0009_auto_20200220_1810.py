# Generated by Django 3.0.2 on 2020-02-20 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0008_auto_20200218_2140'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='module',
            name='matiere-formation',
        ),
        migrations.AlterField(
            model_name='module',
            name='coordinateur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scolar.Enseignant'),
        ),
        migrations.AlterField(
            model_name='module',
            name='periode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scolar.PeriodeProgramme'),
        ),
        migrations.AlterField(
            model_name='modulessuivis',
            name='periode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scolar.PeriodeProgramme'),
        ),
        migrations.AddConstraint(
            model_name='module',
            constraint=models.UniqueConstraint(fields=('matiere', 'formation', 'periode'), name='matiere-formation'),
        ),
    ]
