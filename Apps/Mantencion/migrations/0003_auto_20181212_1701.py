# Generated by Django 2.1.4 on 2018-12-12 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Mantencion', '0002_auto_20181212_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mantencion.Cliente'),
        ),
        migrations.AlterField(
            model_name='orden',
            name='id_ascensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mantencion.Ascensor'),
        ),
        migrations.AlterField(
            model_name='orden',
            name='tecnico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mantencion.Tecnico'),
        ),
    ]