# Generated by Django 2.2.10 on 2023-03-19 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0246_facture'),
    ]

    operations = [
        migrations.AddField(
            model_name='engagement',
            name='facture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='facture', to='scolar.Facture'),
        ),
        migrations.AddField(
            model_name='engagement',
            name='fournisseur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fournisseur', to='scolar.Fournisseur'),
        ),
    ]
