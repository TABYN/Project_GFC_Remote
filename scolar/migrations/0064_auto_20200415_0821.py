# Generated by Django 3.0.2 on 2020-04-15 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0063_auto_20200414_1721'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inscription',
            old_name='moyenne',
            new_name='moy',
        ),
        migrations.AddField(
            model_name='inscription',
            name='moy_post_delib',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='inscriptionperiode',
            name='moy_post_delib',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AddField(
            model_name='resultatue',
            name='moy_post_delib',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]
