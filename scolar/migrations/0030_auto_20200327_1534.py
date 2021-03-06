# Generated by Django 3.0.2 on 2020-03-27 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0029_absenceenseignant_date_justif'),
    ]

    operations = [
        migrations.AddField(
            model_name='seance',
            name='rattrapage',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='situation',
            field=models.CharField(blank=True, choices=[('A', 'En activité'), ('D', 'Mise en disponibilité'), ('T', 'Détachement'), ('M', 'Congé de Maladie'), ('I', 'Invalidité'), ('R', 'Retraité')], default='A', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='statut',
            field=models.CharField(blank=True, choices=[('P', 'Permanent'), ('V', 'Vacataire'), ('A', 'Associé')], default='P', max_length=1, null=True),
        ),
    ]
