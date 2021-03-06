# Generated by Django 3.0.2 on 2020-11-01 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0145_auto_20201031_1014'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeriodeFormation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(blank=True, max_length=20, null=True)),
                ('formation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='periodes', to='scolar.Formation')),
                ('periode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='scolar.Periode')),
            ],
        ),
        migrations.AddConstraint(
            model_name='periodeformation',
            constraint=models.UniqueConstraint(fields=('formation', 'periode'), name='formation-periode'),
        ),
    ]
