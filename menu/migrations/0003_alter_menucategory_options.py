# Generated by Django 4.0.3 on 2022-05-16 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_menucategory_options_alter_menuitem_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menucategory',
            options={'ordering': ['order'], 'verbose_name_plural': 'Menu Categories'},
        ),
    ]
