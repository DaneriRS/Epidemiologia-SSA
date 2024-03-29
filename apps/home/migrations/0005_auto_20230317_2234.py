# Generated by Django 3.2.16 on 2023-03-18 04:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informacionusuario',
            name='jurisdiccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.jurisdiccion', verbose_name='Jurisdiccion'),
        ),
        migrations.AlterField(
            model_name='informacionusuario',
            name='unidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.unidad', verbose_name='Unidad'),
        ),
        migrations.AlterField(
            model_name='informacionusuario',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
