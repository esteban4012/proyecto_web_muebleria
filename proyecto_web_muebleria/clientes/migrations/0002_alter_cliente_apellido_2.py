# Generated by Django 4.2.3 on 2023-07-21 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='apellido_2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
