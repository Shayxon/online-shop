# Generated by Django 5.0.2 on 2024-02-29 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='surename',
            new_name='last_name',
        ),
    ]
