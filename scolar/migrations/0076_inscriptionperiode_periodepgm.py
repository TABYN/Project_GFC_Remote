# Generated by Django 3.0.2 on 2020-06-05 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0075_auto_20200605_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscriptionperiode',
            name='periodepgm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scolar.PeriodeProgramme'),
        ),
    ]
