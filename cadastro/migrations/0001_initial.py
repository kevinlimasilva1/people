# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('idade', models.IntegerField()),
                ('sexo', models.CharField(max_length=1, choices=[('M', 'MASCULINO'), ('F', 'FEMININO')])),
                ('endereco', models.CharField(max_length=200)),
                ('cep', models.IntegerField()),
                ('bairro', models.CharField(max_length=80)),
                ('cidade', models.CharField(max_length=80)),
                ('estado', models.CharField(max_length=2, choices=[('AC', 'ACRE'), ('AL', 'ALAGOAS'), ('AP', 'AMAPA'), ('AM', 'AMAZONAS'), ('BA', 'BAHIA'), ('CE', 'CEARA'), ('DF', 'DISTRITO FEDERAL'), ('ES', 'ESPIRITO SANTO'), ('GO', 'GOIAS'), ('MA', 'MARANHAO'), ('MT', 'MATO GROSSO'), ('MS', 'MATO GROSSO DO SUL'), ('MG', 'MINAS GERAIS'), ('PA', 'PARA'), ('PB', 'PARAIBA'), ('PR', 'PARANA'), ('PE', 'PERNAMBUCO'), ('PI', 'PIAUI'), ('RJ', 'RIO DE JANEIRO'), ('RN', 'RIO GRANDE DO NORTE'), ('RS', 'RIO GRANDE DO SUL'), ('RO', 'RONDONIA'), ('RR', 'RORAIMA'), ('SC', 'SANTA CATARINA'), ('SP', 'SAO PAULO'), ('SE', 'SERGIPE'), ('TO', 'TOCANTINS')])),
                ('cpf', models.IntegerField(max_length=11)),
                ('rg', models.IntegerField(max_length=9)),
                ('email', models.EmailField(max_length=254)),
                ('dtn', models.DateField(default=datetime.datetime(2017, 3, 20, 12, 34, 29, 207076, tzinfo=utc), verbose_name='Data de nascimento')),
                ('dts', models.DateTimeField(blank=True, default=datetime.datetime(2017, 3, 20, 12, 34, 29, 207116, tzinfo=utc), verbose_name='Pessoa salva em')),
            ],
        ),
    ]
