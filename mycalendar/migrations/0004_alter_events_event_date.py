# Generated by Django 4.2 on 2025-01-16 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycalendar', '0003_alter_events_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='event_date',
            field=models.DateField(),
        ),
    ]
