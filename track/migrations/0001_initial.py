# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 02:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bogger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('auto_update_goal', models.BooleanField(default=True)),
                ('current_height', models.FloatField(blank=True, help_text='Height in Inches', null=True)),
                ('current_weight', models.FloatField(blank=True, null=True)),
                ('current_activity_factor', models.FloatField(blank=True, choices=[('1.2', 'Sedentary'), ('1.375', 'Lightly Active'), ('1.55', 'Moderately Active'), ('1.725', 'Very Active'), ('1.9', 'Extra Active')], null=True)),
                ('current_daily_weight_goal', models.FloatField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CalorieEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_type', models.CharField(choices=[('C', 'Consumed (Eaten)'), ('E', 'Expended (Exercise)')], default='C', max_length=1)),
                ('calories', models.IntegerField()),
                ('note', models.CharField(max_length=255)),
                ('dt_created', models.DateTimeField(auto_now_add=True)),
                ('dt_occurred', models.DateTimeField()),
                ('date', models.DateField()),
                ('bogger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='track.Bogger')),
            ],
            options={
                'get_latest_by': 'dt_occurred',
            },
        ),
        migrations.CreateModel(
            name='DailyEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('calories_consumed', models.IntegerField(default=0)),
                ('calories_expended', models.IntegerField(default=0)),
                ('bogger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='track.Bogger')),
            ],
            options={
                'get_latest_by': 'date',
            },
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('daily_weight_goal', models.FloatField(blank=True, null=True)),
                ('dt_created', models.DateTimeField(auto_now_add=True)),
                ('bogger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='track.Bogger')),
            ],
            options={
                'get_latest_by': 'date',
            },
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('height', models.FloatField(blank=True, help_text='Height in Inches', null=True)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('activity_factor', models.FloatField(blank=True, null=True)),
                ('dt_created', models.DateTimeField(auto_now_add=True)),
                ('bogger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='track.Bogger')),
            ],
            options={
                'get_latest_by': 'date',
            },
        ),
        migrations.AlterUniqueTogether(
            name='measurement',
            unique_together=set([('bogger', 'date')]),
        ),
        migrations.AlterUniqueTogether(
            name='goal',
            unique_together=set([('bogger', 'date')]),
        ),
        migrations.AlterUniqueTogether(
            name='dailyentry',
            unique_together=set([('bogger', 'date')]),
        ),
    ]
