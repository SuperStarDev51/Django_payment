# Generated by Django 3.0.5 on 2020-05-17 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(blank=True, choices=[('initiated', 'Initiated'), ('success', 'Success'), ('failed', 'failed'), ('cancelled', 'cancelled')], max_length=30, null=True),
        ),
    ]
