# Generated by Django 3.1.5 on 2021-07-08 18:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('escolta', '0002_auto_20210708_1401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='escoltas',
            name='data_ativacao',
        ),
        migrations.RemoveField(
            model_name='escoltas',
            name='data_inativacao',
        ),
        migrations.RemoveField(
            model_name='escoltas',
            name='motivo_inativacao',
        ),
        migrations.RemoveField(
            model_name='escoltas',
            name='usuario_ativacao',
        ),
        migrations.RemoveField(
            model_name='escoltas',
            name='usuario_inativacao',
        ),
        migrations.AlterField(
            model_name='escoltas',
            name='fase_escolta_aerea',
            field=models.CharField(blank=True, choices=[('AGENDADA', 'Força Aérea Brasileira'), ('INICIADA_TERRESTRE', 'Polícia Federal'), ('INICIADA_AEREA', 'Polícia Rodoviária Federal'), ('EM_TRANSITO', 'Polícia Civil'), ('FINALIZADA', 'Outros')], default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='escoltas',
            name='fase_escolta_terrestre',
            field=models.CharField(blank=True, choices=[('AGENDADA', 'Força Aérea Brasileira'), ('INICIADA_TERRESTRE', 'Polícia Federal'), ('INICIADA_AEREA', 'Polícia Rodoviária Federal'), ('EM_TRANSITO', 'Polícia Civil'), ('FINALIZADA', 'Outros')], default=None, max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='VoosEscolta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voo', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('pedido_inclusao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='escolta.escoltas')),
                ('usuario_cadastro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='usuario_voo_escolta_related', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]