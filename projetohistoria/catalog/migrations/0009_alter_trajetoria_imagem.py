# Generated by Django 4.2.3 on 2023-12-06 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_trajetoria_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trajetoria',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='trumb_trajetoria'),
        ),
    ]
