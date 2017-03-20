# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='dtn',
            field=models.DateField(default=datetime.datetime(2017, 3, 20, 12, 49, 30, 999617, tzinfo=utc), verbose_name='Data de nascimento'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='dts',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 20, 12, 49, 30, 999654, tzinfo=utc), blank=True, verbose_name='Pessoa salva em'),
        ),
    ]
