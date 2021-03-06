# Generated by Django 3.0.2 on 2020-10-25 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0142_pv_moy_ue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscription',
            name='decision_jury',
            field=models.CharField(blank=True, choices=[('C', '//////'), ('A', 'Admis'), ('AR', 'Admis avec Rachat'), ('AC', 'Admis au Concours'), ('R', 'Redouble'), ('F', 'Abandon'), ('M', 'Maladie'), ('M1', 'Congés académique (année blanche) pour raisons médicales'), ('M2', 'Congés académique (année blanche) pour raisons personnelles'), ('M3', 'Congés académique (année blanche) pour raisons personnelles (Covid 19)'), ('M4', 'Congés académique (année blanche) pour raisons familiales'), ('N', 'Non Admis'), ('X', 'Non Inscrit')], default='X', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='proposition_decision_jury',
            field=models.CharField(blank=True, choices=[('C', '//////'), ('A', 'Admis'), ('AR', 'Admis avec Rachat'), ('AC', 'Admis au Concours'), ('R', 'Redouble'), ('F', 'Abandon'), ('M', 'Maladie'), ('M1', 'Congés académique (année blanche) pour raisons médicales'), ('M2', 'Congés académique (année blanche) pour raisons personnelles'), ('M3', 'Congés académique (année blanche) pour raisons personnelles (Covid 19)'), ('M4', 'Congés académique (année blanche) pour raisons familiales'), ('N', 'Non Admis'), ('X', 'Non Inscrit')], default='X', max_length=2, null=True),
        ),
    ]
