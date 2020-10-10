# Generated by Django 3.1.2 on 2020-10-10 01:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import functools
import purpleserver.core.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrier',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(default=functools.partial(purpleserver.core.models.uuid, *(), **{'prefix': 'car_'}), editable=False, max_length=50, primary_key=True, serialize=False)),
                ('carrier_id', models.CharField(help_text='eg. canadapost, dhl_express, fedex, purolator_courrier, ups...', max_length=200, unique=True)),
                ('test', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CanadaPostSettings',
            fields=[
                ('carrier_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='providers.carrier')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('customer_number', models.CharField(max_length=200)),
                ('contract_id', models.CharField(blank=True, default='', max_length=200)),
            ],
            options={
                'verbose_name': 'Canada Post Settings',
                'verbose_name_plural': 'Canada Post Settings',
                'db_table': 'canada-post-settings',
            },
            bases=('providers.carrier',),
        ),
        migrations.CreateModel(
            name='DHLSettings',
            fields=[
                ('carrier_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='providers.carrier')),
                ('site_id', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('account_number', models.CharField(blank=True, default='', max_length=200)),
            ],
            options={
                'verbose_name': 'DHL Express Settings',
                'verbose_name_plural': 'DHL Express Settings',
                'db_table': 'dhl_express-settings',
            },
            bases=('providers.carrier',),
        ),
        migrations.CreateModel(
            name='EShipperSettings',
            fields=[
                ('carrier_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='providers.carrier')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'eShipper Settings',
                'verbose_name_plural': 'eShipper Settings',
                'db_table': 'eshipper-settings',
            },
            bases=('providers.carrier',),
        ),
        migrations.CreateModel(
            name='FedexSettings',
            fields=[
                ('carrier_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='providers.carrier')),
                ('user_key', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('meter_number', models.CharField(max_length=200)),
                ('account_number', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'FedEx Express Settings',
                'verbose_name_plural': 'FedEx Express Settings',
                'db_table': 'fedex_express-settings',
            },
            bases=('providers.carrier',),
        ),
        migrations.CreateModel(
            name='FreightcomSettings',
            fields=[
                ('carrier_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='providers.carrier')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Freightcom Settings',
                'verbose_name_plural': 'Freightcom Settings',
                'db_table': 'freightcom-settings',
            },
            bases=('providers.carrier',),
        ),
        migrations.CreateModel(
            name='PurolatorSettings',
            fields=[
                ('carrier_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='providers.carrier')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('account_number', models.CharField(max_length=200)),
                ('user_token', models.CharField(blank=True, default='', max_length=200)),
            ],
            options={
                'verbose_name': 'Purolator Courier Settings',
                'verbose_name_plural': 'Purolator Courier Settings',
                'db_table': 'purolator_courier-settings',
            },
            bases=('providers.carrier',),
        ),
        migrations.CreateModel(
            name='UPSSettings',
            fields=[
                ('carrier_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='providers.carrier')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('access_license_number', models.CharField(max_length=200)),
                ('account_number', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'UPS Package Settings',
                'verbose_name_plural': 'UPS Package Settings',
                'db_table': 'ups_package-settings',
            },
            bases=('providers.carrier',),
        ),
    ]
