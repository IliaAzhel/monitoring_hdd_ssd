# Generated by Django 3.2 on 2021-04-29 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='state',
            new_name='health',
        ),
        migrations.AlterField(
            model_name='device',
            name='pc_name',
            field=models.CharField(help_text='PC name', max_length=20),
        ),
    ]
