# Generated by Django 3.2.16 on 2023-05-28 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_auto_20230522_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='numExt',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Numero exterior'),
        ),
    ]
