# Generated by Django 3.2.5 on 2021-09-22 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210804_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteneasset',
            name='trx',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.trx'),
        ),
    ]