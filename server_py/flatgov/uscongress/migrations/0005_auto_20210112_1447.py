# Generated by Django 3.1 on 2021-01-12 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uscongress', '0004_auto_20210112_1307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uscongressupdatejob',
            old_name='content',
            new_name='data_content',
        ),
        migrations.AddField(
            model_name='uscongressupdatejob',
            name='bill_list',
            field=models.JSONField(default=list),
        ),
    ]