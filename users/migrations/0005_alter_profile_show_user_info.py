# Generated by Django 4.0.3 on 2022-05-22 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_course_alter_profile_online_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='show_user_info',
            field=models.BooleanField(default=True),
        ),
    ]
