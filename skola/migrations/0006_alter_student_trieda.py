# Generated by Django 5.1.1 on 2024-12-11 10:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skola', '0005_alter_trieda_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='trieda',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='skola.trieda'),
        ),
    ]
