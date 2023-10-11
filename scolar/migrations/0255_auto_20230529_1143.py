# Generated by Django 2.2.10 on 2023-05-29 10:43

from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0254_transfert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercice',
            name='credit_non_allouee',
            field=djmoney.models.fields.MoneyField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='exercice',
            name='total',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, max_digits=9),
        ),
    ]