# Generated by Django 5.1.1 on 2024-12-11 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skola', '0002_ucitel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['priezvisko'], 'verbose_name': 'Študent', 'verbose_name_plural': 'Študenti'},
        ),
        migrations.AlterModelOptions(
            name='ucitel',
            options={'ordering': ['priezvisko'], 'verbose_name': 'Ucitel', 'verbose_name_plural': 'Ucitelia'},
        ),
    ]
