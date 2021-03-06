# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookcases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookshelf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shelf_label', models.CharField(max_length=50)),
                ('bookcase', models.ForeignKey(to='bookcases.Bookcase')),
            ],
            options={
                'ordering': ['shelf_label'],
            },
        ),
    ]
