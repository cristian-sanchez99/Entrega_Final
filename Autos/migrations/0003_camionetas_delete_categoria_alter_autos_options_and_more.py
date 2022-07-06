# Generated by Django 4.0.4 on 2022-06-09 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Autos', '0002_categoria_motocicletas_alter_autos_sku'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camionetas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
                ('price', models.FloatField()),
                ('SKU', models.CharField(max_length=30, unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Camioneta',
                'verbose_name_plural': 'Camionetas',
            },
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.AlterModelOptions(
            name='autos',
            options={'verbose_name': 'Auto', 'verbose_name_plural': 'Autos'},
        ),
        migrations.AlterModelOptions(
            name='motocicletas',
            options={'verbose_name': 'Motocicleta', 'verbose_name_plural': 'Motocicletas'},
        ),
    ]