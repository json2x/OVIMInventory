# Generated by Django 3.2.5 on 2021-09-01 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nmsdata', '0002_rename_ran_cell_cell'),
    ]

    operations = [
        migrations.AddField(
            model_name='cell',
            name='record_status',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='record_status',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='trx',
            name='record_status',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]