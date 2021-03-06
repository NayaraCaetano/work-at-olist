# Generated by Django 2.0.1 on 2018-02-09 19:01

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Call',
            fields=[
                ('call_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('start_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('end_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('call_start', models.DateTimeField(blank=True, null=True)),
                ('call_end', models.DateTimeField(blank=True, null=True)),
                ('source', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True)),
                ('destination', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True)),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
    ]
