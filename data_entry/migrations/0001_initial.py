# Generated by Django 5.0.3 on 2024-03-17 12:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('date', models.DateField(verbose_name='Purchase Date')),
                ('obrNum', models.PositiveSmallIntegerField()),
                ('brand', models.CharField(max_length=100)),
                ('supplier', models.CharField(max_length=100)),
                ('price_per_unit', models.DecimalField(decimal_places=2, help_text='from 0 to 999,999,999.99', max_digits=9)),
                ('qty', models.PositiveSmallIntegerField(default=1)),
                ('status', models.CharField(blank=True, choices=[('Working', 'Working'), ('Not Working', 'Not Working'), ('Turned Over to GSO', 'Turned Over to GSO')], default='Working', max_length=80)),
                ('returned_date', models.DateField()),
                ('notes', models.TextField(blank=True)),
                ('added_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data_entry.category')),
                ('sub_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data_entry.subcategory')),
            ],
        ),
    ]
