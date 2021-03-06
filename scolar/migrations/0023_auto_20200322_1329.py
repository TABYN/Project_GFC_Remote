# Generated by Django 3.0.2 on 2020-03-22 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0022_auto_20200319_2027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='etudiant',
            old_name='genre',
            new_name='sexe',
        ),
        migrations.RemoveField(
            model_name='enseignant',
            name='statut',
        ),
        migrations.AddField(
            model_name='enseignant',
            name='bal',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='enseignant',
            name='bureau',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='enseignant',
            name='eps',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='enseignant',
            name='eps_a',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='enseignant',
            name='nom_a',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='enseignant',
            name='prenom_a',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='enseignant',
            name='sexe',
            field=models.CharField(blank=True, choices=[('M', 'Masculin'), ('F', 'Féminin')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='enseignant',
            name='situation',
            field=models.CharField(blank=True, choices=[('A', 'En activité'), ('D', 'Mise en disponibilité'), ('T', 'Détachement'), ('M', 'Congé de Maladie'), ('I', 'Invalidité')], default='A', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='grade',
            field=models.CharField(blank=True, choices=[('MA.B', 'Maître Assistant B'), ('MA.A', 'Maître Assistant A'), ('MC.B', 'Maître de Conférences B'), ('MC.A', 'Maître de Conférences A'), ('PR', 'Professeur')], max_length=4, null=True),
        ),
    ]
