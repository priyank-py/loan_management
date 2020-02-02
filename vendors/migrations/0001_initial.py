# Generated by Django 2.2.6 on 2019-10-31 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Vendor name')),
                ('phone', models.CharField(max_length=50, verbose_name='Phone number')),
                ('alternate', models.CharField(blank=True, max_length=50, null=True, verbose_name='Alternate number')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Address')),
                ('connection', models.CharField(blank=True, max_length=50, null=True, verbose_name='Connection')),
                ('account_name', models.CharField(max_length=50, verbose_name='Account Name')),
                ('account_number', models.CharField(max_length=50, verbose_name='Account Number')),
                ('bank_branch', models.CharField(max_length=50, verbose_name='Bank Branch')),
                ('ifsc_code', models.CharField(max_length=50, verbose_name='IFSC code')),
                ('gst', models.CharField(blank=True, max_length=50, null=True, verbose_name='GST no.')),
                ('tan', models.CharField(blank=True, max_length=50, null=True, verbose_name='TAN no.')),
                ('pan', models.CharField(blank=True, max_length=50, null=True, verbose_name='PAN no.')),
                ('account_type', models.CharField(blank=True, choices=[('current', 'Current'), ('savings', 'Savings')], max_length=50, null=True, verbose_name='Account Type')),
            ],
            options={
                'verbose_name': 'Vendor',
                'verbose_name_plural': 'Vendors',
            },
        ),
    ]
