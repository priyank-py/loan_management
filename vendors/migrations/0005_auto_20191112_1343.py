# Generated by Django 2.2.6 on 2019-11-12 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0004_auto_20191112_1324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='account_name',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='account_number',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='account_type',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='bank_branch',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='ifsc_code',
        ),
        migrations.CreateModel(
            name='VendorAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Account Name')),
                ('account_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Account Number')),
                ('bank_branch', models.CharField(blank=True, max_length=50, null=True, verbose_name='Bank Branch')),
                ('ifsc_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='IFSC code')),
                ('account_type', models.CharField(blank=True, choices=[('current', 'Current'), ('savings', 'Savings')], max_length=50, null=True, verbose_name='Account Type')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_accounts', to='vendors.Vendor', verbose_name='Vendor')),
            ],
        ),
    ]
