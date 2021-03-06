# Generated by Django 3.2.7 on 2022-01-24 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0007_alter_ticketmessage_ticket_id'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='ticket',
            name='unique',
        ),
        migrations.AddField(
            model_name='ticket',
            name='identical',
            field=models.IntegerField(default=1, unique=True),
        ),
        migrations.AlterField(
            model_name='ticketmessage',
            name='ticket_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.ticket', to_field='identical'),
        ),
    ]
