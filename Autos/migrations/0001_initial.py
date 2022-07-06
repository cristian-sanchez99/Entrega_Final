# Generated by Django 4.0.4 on 2022-06-08 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
                ('price', models.FloatField()),
                ('SKU', models.CharField(max_length=30)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
