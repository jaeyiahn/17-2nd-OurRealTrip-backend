# Generated by Django 3.1.7 on 2021-03-05 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'airlines',
            },
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('code', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'airports',
            },
        ),
        migrations.CreateModel(
            name='FlightStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'flight_statuses',
            },
        ),
        migrations.CreateModel(
            name='FlightSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_code', models.CharField(max_length=45)),
                ('departure_date', models.DateField()),
                ('arrival_date', models.DateField()),
                ('departure_time', models.TimeField()),
                ('arrival_time', models.TimeField()),
                ('duration_time', models.TimeField()),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.airline')),
                ('arrival_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival_airport', to='flight.airport')),
                ('departure_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure_airport', to='flight.airport')),
            ],
            options={
                'db_table': 'flight_schedules',
            },
        ),
        migrations.CreateModel(
            name='FlightPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=30)),
                ('remaining_seat', models.IntegerField()),
                ('flight_schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.flightschedule')),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='flight.flightstatus')),
            ],
            options={
                'db_table': 'flight_prices',
            },
        ),
    ]