# Generated by Django 3.2.4 on 2021-08-30 05:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sneakers', '0021_auto_20210829_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockxanalyze',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
