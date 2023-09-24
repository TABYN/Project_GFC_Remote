# Generated by Django 2.2.10 on 2023-06-08 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0259_mandat_engagement'),
    ]

    operations = [
        migrations.AddField(
            model_name='engagement',
            name='mandat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mandat_engagement', to='scolar.Mandat'),
        ),
    ]
