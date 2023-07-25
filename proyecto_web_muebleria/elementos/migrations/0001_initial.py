# Generated by Django 4.2.3 on 2023-07-21 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Elementos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=30)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=14)),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorias.categoria')),
            ],
        ),
    ]
