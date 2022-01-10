# Generated by Django 3.2.5 on 2022-01-10 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aid', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessConstraint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=250)),
                ('site_id', models.CharField(max_length=250)),
                ('exact_date', models.CharField(max_length=250)),
                ('day_of_month', models.CharField(max_length=250)),
                ('day_of_week', models.CharField(max_length=250)),
                ('start_time', models.CharField(max_length=250)),
                ('end_time', models.CharField(max_length=250)),
                ('restricted_time', models.CharField(max_length=250)),
                ('site_name', models.CharField(max_length=250)),
            ],
        ),
    ]