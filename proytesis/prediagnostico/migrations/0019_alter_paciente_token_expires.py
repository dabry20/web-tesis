# Generated by Django 5.0.7 on 2024-10-05 18:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediagnostico', '0018_alter_paciente_token_alter_paciente_token_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='token_expires',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 5, 19, 4, 44, 496418, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
