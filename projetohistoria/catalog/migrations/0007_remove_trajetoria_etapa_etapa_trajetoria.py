# Generated by Django 4.2.3 on 2023-12-04 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_remove_material_fonte_material_fonteform_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trajetoria',
            name='etapa',
        ),
        migrations.AddField(
            model_name='etapa',
            name='trajetoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.trajetoria'),
        ),
    ]
