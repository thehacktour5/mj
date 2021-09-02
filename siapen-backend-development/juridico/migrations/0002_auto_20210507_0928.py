# Generated by Django 3.1.5 on 2021-05-07 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('juridico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NormasJuridicas',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('ativo', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('delete_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('excluido', models.BooleanField(default=False)),
                ('descricao', models.CharField(max_length=250)),
                ('norma_juridica', models.CharField(choices=[('EMENDA À CONSTITUIÇÃO', 'Emenda à Constituição'), ('LEI COMPLEMENTAR', 'Lei Complementar'), ('LEI ORDINÁRIA', 'Lei Ordinária'), ('LEI DELEGADA', 'Lei Delegada'), ('MEDIDA PROVISÓRIA', 'Medida Provisória'), ('DECRETO LEGISLATIVO', 'Decreto Legislativo'), ('RESOLUÇÃO', 'Resolução')], max_length=100)),
                ('motivo_ativacao', models.TextField(blank=True, default=None, max_length=200, null=True)),
                ('motivo_inativacao', models.TextField(blank=True, default=None, max_length=200, null=True)),
                ('data_ativacao', models.DateTimeField(blank=True, default=None, null=True)),
                ('data_inativacao', models.DateTimeField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'Norma Jurídica',
                'verbose_name_plural': 'Normas Jurídicas',
            },
        ),
        migrations.CreateModel(
            name='TituloLei',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('ativo', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('delete_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('excluido', models.BooleanField(default=False)),
                ('norma_juridica', models.CharField(choices=[('EMENDA À CONSTITUIÇÃO', 'Emenda à Constituição'), ('LEI COMPLEMENTAR', 'Lei Complementar'), ('LEI ORDINÁRIA', 'Lei Ordinária'), ('LEI DELEGADA', 'Lei Delegada'), ('MEDIDA PROVISÓRIA', 'Medida Provisória'), ('DECRETO LEGISLATIVO', 'Decreto Legislativo'), ('RESOLUÇÃO', 'Resolução')], max_length=50)),
                ('nome', models.CharField(max_length=255)),
                ('motivo_ativacao', models.TextField(blank=True, default=None, max_length=200, null=True)),
                ('motivo_inativacao', models.TextField(blank=True, default=None, max_length=200, null=True)),
                ('data_ativacao', models.DateTimeField(blank=True, default=None, null=True)),
                ('data_inativacao', models.DateTimeField(blank=True, default=None, null=True)),
                ('usuario_cadastro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('usuario_edicao', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updatedjuridico_titulolei_related', to=settings.AUTH_USER_MODEL)),
                ('usuario_exclusao', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='deletejuridico_titulolei_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='pedidoinclusao',
            name='autorizador',
        ),
        migrations.RemoveField(
            model_name='pedidoinclusao',
            name='pessoa',
        ),
        migrations.RemoveField(
            model_name='pedidoinclusao',
            name='solicitante',
        ),
        migrations.RemoveField(
            model_name='pedidoinclusao',
            name='usuario_cadastro',
        ),
        migrations.RemoveField(
            model_name='procedimentodisciplinar',
            name='unidade_cadastradora',
        ),
        migrations.RemoveField(
            model_name='procedimentodisciplinar',
            name='usuario_cadastro',
        ),
        migrations.RemoveField(
            model_name='procedimentointernofalta',
            name='falta',
        ),
        migrations.RemoveField(
            model_name='procedimentointernofalta',
            name='interno',
        ),
        migrations.RemoveField(
            model_name='procedimentointernofalta',
            name='procedimento',
        ),
        migrations.DeleteModel(
            name='AutorizadorInclusao',
        ),
        migrations.DeleteModel(
            name='FaltaDisciplinar',
        ),
        migrations.DeleteModel(
            name='PedidoInclusao',
        ),
        migrations.DeleteModel(
            name='ProcedimentoDisciplinar',
        ),
        migrations.DeleteModel(
            name='ProcedimentoInternoFalta',
        ),
        migrations.AddField(
            model_name='normasjuridicas',
            name='titulo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='juridico.titulolei'),
        ),
        migrations.AddField(
            model_name='normasjuridicas',
            name='usuario_cadastro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='normasjuridicas',
            name='usuario_edicao',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updatedjuridico_normasjuridicas_related', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='normasjuridicas',
            name='usuario_exclusao',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='deletejuridico_normasjuridicas_related', to=settings.AUTH_USER_MODEL),
        ),
    ]