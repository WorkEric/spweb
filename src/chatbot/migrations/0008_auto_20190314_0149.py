# Generated by Django 2.1.1 on 2019-03-14 01:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0007_auto_20190313_1036'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceFeature_PricePlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255, validators=[django.core.validators.MaxLengthValidator(255)])),
                ('Freevalue', models.CharField(blank=True, max_length=255, validators=[django.core.validators.MaxLengthValidator(255)])),
                ('Litevalue', models.CharField(blank=True, max_length=255, validators=[django.core.validators.MaxLengthValidator(255)])),
                ('Standardvalue', models.CharField(blank=True, max_length=255, validators=[django.core.validators.MaxLengthValidator(255)])),
                ('Plusvalue', models.CharField(blank=True, max_length=255, validators=[django.core.validators.MaxLengthValidator(255)])),
            ],
            options={
                'db_table': 'pricefeature_priceplan',
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='pricefeature',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='priceplanfeature',
            options={'managed': True},
        ),
    ]
