# Generated by Django 3.2.4 on 2021-06-14 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_broadcastid_access_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='broadcastid',
            name='broadcast_id',
        ),
        migrations.RemoveField(
            model_name='broadcastid',
            name='username',
        ),
    ]
