# Generated by Django 3.2.16 on 2023-04-23 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_registroestudio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='numAfiliacion',
            field=models.CharField(max_length=50, unique=True, verbose_name='Numero de afiliacion'),
        ),
    ]
