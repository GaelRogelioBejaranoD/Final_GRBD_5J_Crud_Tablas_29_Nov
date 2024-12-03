# Generated by Django 5.1.1 on 2024-12-02 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('telefono', models.PositiveIntegerField()),
                ('direccion', models.CharField(max_length=100)),
                ('membresia_activa', models.BooleanField()),
                ('dias_restantes_mem', models.PositiveIntegerField()),
                ('fecha_ingreso', models.DateField()),
            ],
        ),
    ]