# Generated by Django 3.0.2 on 2020-09-04 17:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0113_auto_20200904_0811'),
    ]

    operations = [
        migrations.AddField(
            model_name='pfe',
            name='antecedents',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='pfe',
            name='email_promoteur',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='pfe',
            name='moyens_informatiques',
            field=models.CharField(choices=[('ESI', "A la charge de l'école"), ('ORG', "A la charge de l'organisme d'accueil")], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='pfe',
            name='resultats_attendus',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='pfe',
            name='tel_promoteur',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator('^[0-9\\+]*$', "Que des chiffres et le + pour l'international")]),
        ),
    ]
