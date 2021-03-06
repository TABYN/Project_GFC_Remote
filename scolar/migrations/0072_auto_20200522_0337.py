# Generated by Django 3.0.2 on 2020-05-22 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0071_auto_20200508_0343'),
    ]

    operations = [
        migrations.AddField(
            model_name='matiere',
            name='precision',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='matiere',
            name='code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='resultat',
            name='resultat_ue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resultat_matieres', to='scolar.ResultatUE'),
        ),
    ]
