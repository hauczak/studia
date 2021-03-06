# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20171115_1811'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='issue',
            options={'ordering': ('-date',), 'verbose_name': 'Numer', 'verbose_name_plural': 'Numery'},
        ),
        migrations.RemoveField(
            model_name='issue',
            name='index_page_visible',
        ),
        migrations.AddField(
            model_name='issue',
            name='current',
            field=models.BooleanField(default=False, verbose_name='To jest aktualny numer'),
        ),
        migrations.AlterField(
            model_name='customflatpage',
            name='order',
            field=models.DecimalField(blank=True, decimal_places=0, default=99, max_digits=2, null=True, verbose_name='Kolejność w menu'),
        ),
        migrations.AlterField(
            model_name='customflatpage',
            name='title',
            field=models.CharField(help_text='Używany na górze strony', max_length=70, verbose_name='Tytuł'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='short_description',
            field=models.TextField(blank=True, help_text='Wyświetlany jeśli nie ma żadnych artykułów.', null=True, verbose_name='Krótki opis'),
        ),
    ]
