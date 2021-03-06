# Generated by Django 3.1.5 on 2021-07-08 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("escolta", "0003_auto_20210708_1520")]

    operations = [
        migrations.RenameField(
            model_name="voosescolta", old_name="pedido_inclusao", new_name="escolta"
        ),
        migrations.AlterField(
            model_name="escoltas",
            name="fase_escolta_aerea",
            field=models.CharField(
                blank=True,
                choices=[
                    ("AGENDADA", "Agendada"),
                    ("INICIADA_TERRESTRE", "Iniciada Escolta Terrestre"),
                    ("INICIADA_AEREA", "Iniciada Escolta Aérea"),
                    ("EM_TRANSITO", "Em Trânsito"),
                    ("FINALIZADA", "Finalizada"),
                ],
                default=None,
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="escoltas",
            name="fase_escolta_terrestre",
            field=models.CharField(
                blank=True,
                choices=[
                    ("AGENDADA", "Agendada"),
                    ("INICIADA_TERRESTRE", "Iniciada Escolta Terrestre"),
                    ("INICIADA_AEREA", "Iniciada Escolta Aérea"),
                    ("EM_TRANSITO", "Em Trânsito"),
                    ("FINALIZADA", "Finalizada"),
                ],
                default=None,
                max_length=20,
                null=True,
            ),
        ),
    ]
