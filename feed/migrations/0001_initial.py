# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='agent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('photo', models.URLField()),
                ('info', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='floor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('floor', models.URLField()),
                ('createdat', models.DateTimeField()),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.URLField()),
                ('createdat', models.DateTimeField()),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='propertyfinder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reference_number', models.CharField(unique=True, max_length=50)),
                ('offering_type', models.CharField(max_length=50, choices=[(b'CS', b'Commercial property for sale'), (b'CR', b'Commercial property for rent'), (b'RS', b'Residential property for sale'), (b'RR', b'Residential property for rent')])),
                ('property_type', models.CharField(max_length=50)),
                ('price_on_application', models.BooleanField(default=None)),
                ('price', models.FloatField()),
                ('service_charge', models.IntegerField()),
                ('rental_period', models.CharField(max_length=20)),
                ('cheques', models.IntegerField(max_length=10)),
                ('city', models.CharField(max_length=50)),
                ('community', models.CharField(max_length=50)),
                ('sub_community', models.CharField(max_length=50)),
                ('property_name', models.CharField(max_length=50)),
                ('title_en', models.CharField(max_length=50)),
                ('title_ar', models.CharField(max_length=50)),
                ('description_en', models.TextField()),
                ('description_ar', models.TextField()),
                ('private_amenities', models.CharField(max_length=30)),
                ('commercial_amenities', models.CharField(max_length=40)),
                ('view', models.TextField()),
                ('plot_size', models.IntegerField()),
                ('size', models.IntegerField()),
                ('bedroom', models.IntegerField()),
                ('bathroom', models.IntegerField()),
                ('featured', models.CharField(max_length=5)),
                ('developer', models.CharField(max_length=50)),
                ('build_year', models.IntegerField()),
                ('floors_number', models.IntegerField()),
                ('stories', models.IntegerField()),
                ('parking', models.IntegerField()),
                ('furnished', models.CharField(max_length=10)),
                ('view360', models.URLField(max_length=300)),
                ('geopoints', models.CharField(max_length=300)),
                ('agent', models.ForeignKey(to='feed.agent')),
                ('floor', models.ForeignKey(to='feed.floor')),
                ('photo', models.ForeignKey(to='feed.photo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
