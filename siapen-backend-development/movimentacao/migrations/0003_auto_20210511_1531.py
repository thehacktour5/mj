# Generated by Django 3.1.5 on 2021-05-11 18:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movimentacao', '0002_fasespedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='fasespedido',
            name='data_ativacao',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='fasespedido',
            name='data_inativacao',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='fasespedido',
            name='motivo_ativacao',
            field=models.TextField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='fasespedido',
            name='motivo_inativacao',
            field=models.TextField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='fasespedido',
            name='usuario_ativacao',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Ativacao_fases_related', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fasespedido',
            name='usuario_inativacao',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Inativação_fases_related', to=settings.AUTH_USER_MODEL),
        ),
    ]