# Generated by Django 2.1.4 on 2018-12-13 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mantencion', '0003_auto_20181212_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orden',
            name='tecnico',
        ),
        migrations.AddField(
            model_name='orden',
            name='tecnico',
            field=models.ManyToManyField(to='Mantencion.Tecnico'),
        ),
    ]