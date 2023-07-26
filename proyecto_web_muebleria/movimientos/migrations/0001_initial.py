# Generated by Django 4.2.3 on 2023-07-21 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('elementos', '0001_initial'),
        ('ordenes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=4)),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=15)),
                ('id_elemento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elementos.elementos')),
                ('id_orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordenes.orden')),
            ],
        ),
    ]