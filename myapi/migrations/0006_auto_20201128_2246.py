# Generated by Django 3.1.3 on 2020-11-28 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0005_delete_hero'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orbitalelement',
            old_name='A1',
            new_name='a1',
        ),
        migrations.RenameField(
            model_name='orbitalelement',
            old_name='A2',
            new_name='a2',
        ),
        migrations.RenameField(
            model_name='orbitalelement',
            old_name='A3',
            new_name='a3',
        ),
        migrations.RenameField(
            model_name='orbitalelement',
            old_name='DT',
            new_name='dt',
        ),
        migrations.RenameField(
            model_name='orbitalelement',
            old_name='Epoch',
            new_name='epoch',
        ),
        migrations.RenameField(
            model_name='orbitalelement',
            old_name='I',
            new_name='i',
        ),
        migrations.RenameField(
            model_name='orbitalelement',
            old_name='MOID',
            new_name='moid',
        ),
        migrations.RenameField(
            model_name='orbitalelement',
            old_name='Node',
            new_name='node',
        ),
        migrations.RenameField(
            model_name='orbitalelement',
            old_name='Object',
            new_name='object',
        ),
        migrations.RenameField(
            model_name='orbitalelement',
            old_name='Object_name',
            new_name='object_name',
        ),
        migrations.RenameField(
            model_name='orbitalelement',
            old_name='P',
            new_name='p',
        ),
        migrations.RenameField(
            model_name='orbitalelement',
            old_name='Ql',
            new_name='ql',
        ),
        migrations.RenameField(
            model_name='orbitalelement',
            old_name='TP',
            new_name='tp',
        ),
    ]
