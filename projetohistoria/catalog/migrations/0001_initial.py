# Generated by Django 4.2.3 on 2023-11-29 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ana',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ana', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Etapa',
            fields=[
                ('numeração', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
                ('IdEtapa', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]
