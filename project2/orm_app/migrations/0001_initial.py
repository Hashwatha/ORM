# Generated by Django 5.0.2 on 2024-03-15 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Railway',
            fields=[
                ('train_no', models.IntegerField(primary_key=True, serialize=False)),
                ('train_name', models.CharField(max_length=50)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('start_station_code', models.CharField(max_length=10)),
                ('end_station_code', models.CharField(max_length=10)),
            ],
        ),
    ]
