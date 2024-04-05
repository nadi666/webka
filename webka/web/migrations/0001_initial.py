# Generated by Django 5.0.4 on 2024-04-05 12:42

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DailyReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_name', models.CharField(max_length=50, null=True)),
                ('report_address', models.CharField(max_length=250, null=True)),
                ('report_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('report_sum', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.manager')),
            ],
        ),
    ]
