# Generated by Django 3.1.7 on 2021-04-22 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scolar', '0161_article_chapitre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='chapitre',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='scolar.chapitre'),
        ),
    ]
