# Generated by Django 3.1 on 2020-12-01 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0016_bill_related_dict'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='es_similarity',
            field=models.JSONField(default=list),
        ),
    ]