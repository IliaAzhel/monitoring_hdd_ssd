# Generated by Django 3.2 on 2021-05-19 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_remove_smart_device'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smartctl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Num', models.CharField(default='ID', help_text='Id', max_length=30)),
                ('Name', models.CharField(help_text='Name', max_length=30, null=True)),
                ('Current', models.CharField(help_text='Current', max_length=30, null=True)),
                ('Trash', models.CharField(help_text='Trash', max_length=30, null=True)),
                ('Type', models.CharField(help_text='Type', max_length=30, null=True)),
                ('RawValue', models.CharField(help_text='RawValue', max_length=30, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Smart',
        ),
    ]