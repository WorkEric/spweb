# Generated by Django 2.1.1 on 2019-03-11 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0005_auto_20190311_2301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricepayment',
            name='end_at',
        ),
        migrations.RemoveField(
            model_name='pricepayment',
            name='start_at',
        ),
    ]