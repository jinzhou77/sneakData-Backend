# Generated by Django 3.2.4 on 2021-08-30 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sneakers', '0025_auto_20210830_0014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockx',
            old_name='id',
            new_name='analyze_id',
        ),
    ]
