# Generated by Django 3.2.7 on 2022-02-09 10:05

import datetime
from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0014_alter_ticket_identical'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='created_at',
            field=django_jalali.db.models.jDateTimeField(default=datetime.datetime.now),
        ),
    ]