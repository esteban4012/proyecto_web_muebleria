# Generated by Django 4.2.3 on 2023-07-27 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elementos', '0001_initial'),
        ('ordenes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='cantidad',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orden',
            name='id_elemento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='elementos.elementos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orden',
            name='valor_total',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=15),
            preserve_default=False,
        ),
    ]