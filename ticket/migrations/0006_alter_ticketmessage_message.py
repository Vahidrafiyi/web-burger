# Generated by Django 3.2.7 on 2022-01-24 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0005_auto_20220124_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketmessage',
            name='message',
            field=models.TextField(),
        ),
    ]