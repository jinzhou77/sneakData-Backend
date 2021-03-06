# Generated by Django 3.2.5 on 2021-07-11 15:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sneakers', '0003_alter_detail_averagesaleprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trades',
            fields=[
                ('trade_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('trade_name', models.CharField(max_length=255, null=True)),
                ('ticker', models.CharField(max_length=255, null=True)),
                ('trade_date', models.DateTimeField()),
                ('trade_size', models.CharField(max_length=255)),
            ],
        ),
    ]
