# Generated by Django 3.2.16 on 2023-04-26 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_informacionusuario_unidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(blank=True, max_length=250, null=True, verbose_name='Titulo')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='media/logos/', verbose_name='ImagenLogo')),
                ('actualizado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
