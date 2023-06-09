# Generated by Django 4.2.1 on 2023-05-26 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_flight_current_seats_alter_flight_destination_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Booking ID')),
                ('seat_num', models.IntegerField(default=0)),
                ('flight_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.flight')),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Passenger ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentProv',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Payment Provider ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Transaction ID')),
                ('payment_prov_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.paymentprov')),
                ('seat_booking_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.booking')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='passenger_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.passenger'),
        ),
    ]
