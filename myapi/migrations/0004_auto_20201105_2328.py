# Generated by Django 3.1.3 on 2020-11-05 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_auto_20201105_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orbitalelement',
            name='A1',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='orbitalelement',
            name='A2',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='orbitalelement',
            name='A3',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='orbitalelement',
            name='DT',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
