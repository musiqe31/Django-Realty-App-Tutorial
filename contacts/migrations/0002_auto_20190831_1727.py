# Generated by Django 2.2.4 on 2019-08-31 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='list_id',
            new_name='listing_id',
        ),
    ]
