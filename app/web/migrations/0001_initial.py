# Generated by Django 3.2 on 2021-05-19 23:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serialNumber', models.CharField(default='num', help_text='serialNumber', max_length=40)),
                ('modelFamily', models.CharField(help_text='ModelFamily', max_length=50, null=True)),
                ('deviceModel', models.CharField(help_text='DeviceModel', max_length=40, null=True)),
                ('userCapacity', models.CharField(help_text='UserCapacity', max_length=40, null=True)),
                ('sectorSizes', models.CharField(help_text='SectorSizes', max_length=40, null=True)),
                ('rotationRate', models.CharField(help_text='Rotation Rate', max_length=40, null=True)),
                ('ataVersion', models.CharField(default='ata', help_text='ATA Version is', max_length=40)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Smart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Num', models.CharField(default='ID', help_text='Id', max_length=30)),
                ('Name', models.CharField(help_text='Name', max_length=30, null=True)),
                ('Current', models.CharField(help_text='Current', max_length=30, null=True)),
                ('Trash', models.CharField(help_text='Trash', max_length=30, null=True)),
                ('Type', models.CharField(help_text='Type', max_length=30, null=True)),
                ('RawValue', models.CharField(help_text='RawValue', max_length=30, null=True)),
                ('device', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.device')),
            ],
        ),
    ]
