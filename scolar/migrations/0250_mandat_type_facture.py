# Generated by Django 2.2.10 on 2023-03-21 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0249_auto_20230320_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='mandat',
            name='type_facture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Type_Facture_mandat', to='scolar.Type_Facture'),
        ),
    ]