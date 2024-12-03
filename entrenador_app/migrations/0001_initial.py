# Generated by Django 5.1.1 on 2024-12-02 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entrenador',
            fields=[
                ('id_entrenador', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('especialidad', models.CharField(max_length=100)),
                ('telefono', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('estado', models.BooleanField()),
                ('horario', models.CharField(max_length=20)),
            ],
        ),
    ]