# Generated by Django 3.1.8 on 2021-06-08 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='eventId',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='referenceUrl',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='sourceId',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]