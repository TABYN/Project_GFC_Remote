# Generated by Django 3.0.2 on 2020-02-15 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulessuivis',
            name='periode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='scolar.Periode'),
        ),
        migrations.AddField(
            model_name='resultat',
            name='acquis',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='resultat',
            name='groupe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='scolar.Groupe'),
        ),
        migrations.AddConstraint(
            model_name='module',
            constraint=models.UniqueConstraint(fields=('matiere', 'formation'), name='matiere-formation'),
        ),
    ]
