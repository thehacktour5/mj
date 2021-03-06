# Generated by Django 3.1.5 on 2021-07-07 17:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("pessoas", "0016_auto_20210702_1444")]

    operations = [
        migrations.AlterField(
            model_name="visitante",
            name="cpf",
            field=models.CharField(
                blank=True,
                max_length=14,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="CPF inválido",
                        regex="[0-9]{3}\\.?[0-9]{3}\\.?[0-9]{3}\\-?[0-9]{2}",
                    )
                ],
            ),
        )
    ]
