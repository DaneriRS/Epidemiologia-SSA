# Generated by Django 3.2.16 on 2023-04-23 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20230423_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localidad',
            name='clave',
            field=models.CharField(max_length=50, verbose_name='Clave'),
        ),
    ]