# Generated by Django 5.1.1 on 2024-12-02 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrenador_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrenador',
            name='horario',
            field=models.CharField(max_length=100),
        ),
    ]
