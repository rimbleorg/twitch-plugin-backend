# Generated by Django 3.2.4 on 2021-06-10 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BroadCastId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('broadcast_id', models.CharField(max_length=100)),
            ],
        ),
    ]