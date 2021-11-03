# Generated by Django 2.2.10 on 2021-10-20 10:08

from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0175_auto_20211020_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit',
            name='credit_allouee',
            field=djmoney.models.fields.MoneyField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='credit',
            name='credit_allouee_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('DZD', 'DZD')], default='XYZ', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='credit',
            name='credit_reste',
            field=djmoney.models.fields.MoneyField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='credit',
            name='credit_reste_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('DZD', 'DZD')], default='XYZ', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='piece',
            name='montant',
            field=djmoney.models.fields.MoneyField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='piece',
            name='montant_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('DZD', 'DZD')], default='XYZ', editable=False, max_length=3),
        ),
    ]
