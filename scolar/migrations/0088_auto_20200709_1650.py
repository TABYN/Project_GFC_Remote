# Generated by Django 3.0.2 on 2020-07-09 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0087_auto_20200705_0619'),
    ]

    operations = [
        migrations.CreateModel(
            name='PV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('annuel', models.BooleanField(default=False)),
                ('tri_rang', models.BooleanField(default=True)),
                ('photo', models.BooleanField(default=True)),
                ('anonyme', models.BooleanField(default=False)),
                ('note_eliminatoire', models.BooleanField(default=True)),
                ('rang', models.BooleanField(default=True)),
                ('signature', models.BooleanField(default=True)),
                ('formation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scolar.Formation')),
                ('periode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scolar.Periode')),
            ],
        ),
        migrations.AddConstraint(
            model_name='pv',
            constraint=models.UniqueConstraint(fields=('formation', 'annuel', 'periode', 'tri_rang', 'photo', 'anonyme', 'note_eliminatoire', 'rang', 'signature'), name='pv_config'),
        ),
    ]
