# Generated by Django 2.2.10 on 2022-12-06 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0237_auto_20221206_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='mandat',
            name='engagement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='engagement', to='scolar.Engagement'),
        ),
    ]
