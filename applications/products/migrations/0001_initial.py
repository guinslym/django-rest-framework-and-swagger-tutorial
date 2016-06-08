# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Name', max_length=255)),
                ('description', models.TextField(verbose_name='Description')),
                ('price', models.FloatField(verbose_name='Price in EUR')),
                ('color', models.PositiveIntegerField(verbose_name='Color', choices=[(1, 'Aquamarine'), (2, 'Blue'), (3, 'Crimson'), (4, 'Fuscia'), (5, 'Goldenrod'), (6, 'Green'), (7, 'Indigo'), (8, 'Khaki'), (9, 'Maroon'), (10, 'Mauv'), (11, 'Orange'), (12, 'Pink'), (13, 'Puce'), (14, 'Purple'), (15, 'Red'), (16, 'Teal'), (17, 'Turquoise'), (18, 'Violet'), (19, 'Yellow')])),
                ('created_date', models.DateTimeField(null=True, verbose_name='Creation Date', auto_now=True)),
                ('in_stock', models.BooleanField(verbose_name='Is available in stock')),
            ],
        ),
    ]
