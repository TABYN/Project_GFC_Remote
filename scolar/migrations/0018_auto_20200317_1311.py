# Generated by Django 3.0.2 on 2020-03-17 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0017_auto_20200316_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultat',
            name='ects',
            field=models.CharField(blank=True, choices=[('A', 'Excellent: 10%'), ('B', 'Très bien: 25%'), ('C', 'Bien: 30%'), ('D', 'Satisfaisant; 25%'), ('E', 'Passable: 10%'), ('Fx', 'Insuffisant'), ('F', 'Insuffisant')], default='F', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='resultat',
            name='ects_post_delib',
            field=models.CharField(blank=True, choices=[('A', 'Excellent: 10%'), ('B', 'Très bien: 25%'), ('C', 'Bien: 30%'), ('D', 'Satisfaisant; 25%'), ('E', 'Passable: 10%'), ('Fx', 'Insuffisant'), ('F', 'Insuffisant')], default='F', max_length=2, null=True),
        ),
    ]
