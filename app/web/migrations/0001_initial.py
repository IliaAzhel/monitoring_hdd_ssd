# Generated by Django 3.2 on 2021-04-27 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Device name', max_length=40)),
                ('temperature', models.CharField(help_text='Device temperature', max_length=20)),
                ('state', models.CharField(help_text='Device state', max_length=20)),
                ('pc_name', models.CharField(help_text='Device name', max_length=20)),
                ('last_update', models.DateField(blank=True, null=True)),
                ('type_of_device', models.CharField(blank=True, choices=[('S', 'SSD'), ('H', 'HDD')], default='HDD', help_text='SSD or HDD', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='web.device')),
                ('metadata', models.CharField(help_text='Metadata', max_length=30)),
            ],
        ),
    ]