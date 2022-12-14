# Generated by Django 4.0.6 on 2022-08-16 08:36

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
            name='chart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
                ('choices', models.CharField(choices=[('Time Chart', 'Time Chart'), ('Integer Chart', 'Integer Chart')], max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('int_value', models.DecimalField(blank=True, decimal_places=2, max_digits=25, null=True)),
                ('time_value', models.TimeField(blank=True, null=True)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('chart', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='index.chart')),
            ],
        ),
    ]
