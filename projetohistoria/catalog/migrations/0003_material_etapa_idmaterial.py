# Generated by Django 4.2.3 on 2023-11-29 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_trajetoria_delete_ana'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('Titulo', models.CharField(max_length=200)),
                ('Tipo', models.CharField(blank=True, max_length=200, null=True)),
                ('Assunto', models.CharField(blank=True, max_length=200, null=True)),
                ('Fonte', models.URLField()),
                ('IdMaterial', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('DataPublicação', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='etapa',
            name='IdMaterial',
            field=models.ManyToManyField(to='catalog.material'),
        ),
    ]
