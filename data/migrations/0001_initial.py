# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 01:00
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discretizacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Discretização',
                'verbose_name_plural': 'Discretizações',
            },
        ),
        migrations.CreateModel(
            name='Fonte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Localizacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordenadas', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='NivelConsistencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Nível de Consistência',
                'verbose_name_plural': 'Níveis de Consistência',
            },
        ),
        migrations.CreateModel(
            name='Posto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_ana', models.CharField(max_length=15, null=True)),
                ('nome', models.CharField(max_length=30)),
                ('fonte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Fonte')),
                ('localizacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Localizacao')),
            ],
        ),
        migrations.CreateModel(
            name='Reducao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Redução',
                'verbose_name_plural': 'Reduções',
            },
        ),
        migrations.CreateModel(
            name='SerieOriginal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo_Fonte_data', models.DateTimeField(auto_now_add=True, verbose_name='Data e Hora')),
                ('serie_temporal_id', models.CharField(choices=[('ok', 'teste')], max_length=1)),
                ('discretizacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Discretizacao')),
                ('posto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Posto')),
                ('tipo_dado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.NivelConsistencia')),
            ],
            options={
                'verbose_name': 'Série Original',
                'verbose_name_plural': 'Séries Originais',
            },
        ),
        migrations.CreateModel(
            name='SerieReduzida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie_temporal_id', models.CharField(choices=[('ok', 'teste')], max_length=1)),
                ('discretizacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Discretizacao')),
                ('reducao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Reducao')),
                ('serie_original', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.SerieOriginal')),
            ],
            options={
                'verbose_name': 'Série Reduzida',
                'verbose_name_plural': 'Séries Reduzidas',
            },
        ),
        migrations.CreateModel(
            name='SerieTemporal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id', models.IntegerField()),
                ('dado', models.FloatField()),
                ('data_e_hora', models.DateTimeField(verbose_name='Data e Hora')),
            ],
            options={
                'verbose_name': 'Série Temporal',
                'verbose_name_plural': 'Séries Temporais',
            },
        ),
        migrations.CreateModel(
            name='TipoPosto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Tipo de Posto',
                'verbose_name_plural': 'Tipos de Posto',
            },
        ),
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Unidade de Medida',
                'verbose_name_plural': 'Unidades de Medida',
            },
        ),
        migrations.CreateModel(
            name='Variavel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variavel', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Variável',
                'verbose_name_plural': 'Variáveis',
            },
        ),
        migrations.AlterUniqueTogether(
            name='serietemporal',
            unique_together=set([('Id', 'data_e_hora')]),
        ),
        migrations.AddField(
            model_name='serieoriginal',
            name='unidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Unidade'),
        ),
        migrations.AddField(
            model_name='serieoriginal',
            name='variavel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Variavel'),
        ),
        migrations.AddField(
            model_name='posto',
            name='tipo_posto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.TipoPosto'),
        ),
    ]
