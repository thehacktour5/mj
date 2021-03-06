# Generated by Django 3.1.5 on 2021-07-08 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("escolta", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="escoltas",
            name="fase_escolta_aerea",
            field=models.CharField(
                choices=[
                    ("AGENDADA", "Força Aérea Brasileira"),
                    ("INICIADA_TERRESTRE", "Polícia Federal"),
                    ("INICIADA_AEREA", "Polícia Rodoviária Federal"),
                    ("EM_TRANSITO", "Polícia Civil"),
                    ("FINALIZADA", "Outros"),
                ],
                default="AGENDADA",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="escoltas",
            name="fase_escolta_terrestre",
            field=models.CharField(
                choices=[
                    ("AGENDADA", "Força Aérea Brasileira"),
                    ("INICIADA_TERRESTRE", "Polícia Federal"),
                    ("INICIADA_AEREA", "Polícia Rodoviária Federal"),
                    ("EM_TRANSITO", "Polícia Civil"),
                    ("FINALIZADA", "Outros"),
                ],
                default="AGENDADA",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="escoltas",
            name="numero_escolta",
            field=models.CharField(default="-", max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="escoltas",
            name="tipo_escolta",
            field=models.CharField(
                blank=True,
                choices=[("INCLUSAO", "INCLUSÃO")],
                default=None,
                max_length=20,
                null=True,
            ),
        ),
    ]
