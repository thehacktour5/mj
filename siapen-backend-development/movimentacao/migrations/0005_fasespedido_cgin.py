# Generated by Django 3.1.5 on 2021-05-21 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("movimentacao", "0004_auto_20210520_1042")]

    operations = [
        migrations.AddField(
            model_name="fasespedido",
            name="cgin",
            field=models.BooleanField(default=False),
        )
    ]
