# Generated by Django 3.2 on 2023-05-10 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0209_auto_20221220_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type_Facture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('type', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='engagement',
            name='fournisseur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fournisseur', to='scolar.fournisseur'),
        ),
        migrations.AddField(
            model_name='engagement',
            name='mandat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mandat_engagement', to='scolar.mandat'),
        ),
        migrations.AddField(
            model_name='fournisseur',
            name='banque',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='banque', to='scolar.banque'),
        ),
        migrations.AlterField(
            model_name='engagement',
            name='type',
            field=models.CharField(choices=[('Prise en charge', 'Prise en charge'), ('Depence', 'Depence'), ('Fiche de regularisation de la provision', 'Fiche de regularisation de la provision')], default='', max_length=60, null=True),
        ),
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_fact', models.IntegerField(null=True)),
                ('date_fact', models.DateField(blank=True, null=True)),
                ('type_facture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Type_Facture', to='scolar.type_facture')),
            ],
        ),
        migrations.AddField(
            model_name='engagement',
            name='facture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='facture', to='scolar.facture'),
        ),
        migrations.AddField(
            model_name='mandat',
            name='type_facture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Type_Facture_mandat', to='scolar.type_facture'),
        ),
    ]
