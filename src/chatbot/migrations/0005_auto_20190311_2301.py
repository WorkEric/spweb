# Generated by Django 2.1.1 on 2019-03-11 23:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0004_auto_20190226_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTemplateContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sp_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='chatbot.SpUser')),
                ('template_content', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='chatbot.TemplateContent')),
            ],
            options={
                'db_table': 'user_template_content',
            },
        ),
        migrations.AddField(
            model_name='pricepayment',
            name='duration',
            field=models.IntegerField(default=0, validators=[django.core.validators.validate_integer]),
        ),
        migrations.AddField(
            model_name='priceplanfeature',
            name='value',
            field=models.CharField(blank=True, max_length=255, validators=[django.core.validators.MaxLengthValidator(255)]),
        ),
    ]
