# Generated by Django 2.2.10 on 2022-10-26 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0212_auto_20221025_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='engagement',
            name='credit_S2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='credit_S2', to='scolar.Credit_S2'),
        ),
    ]
