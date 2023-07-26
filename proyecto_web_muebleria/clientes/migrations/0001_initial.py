# Generated by Django 4.2.3 on 2023-07-21 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('apellido_2', models.CharField(max_length=20)),
                ('numero_identificacion', models.IntegerField()),
                ('direccion', models.CharField(max_length=20)),
                ('telefono', models.IntegerField()),
                ('correo', models.CharField(max_length=30)),
            ],
        ),
    ]