# Generated by Django 2.2.8 on 2020-02-02 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0005_auto_20191112_1343'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vendor',
            options={'verbose_name': 'Customer', 'verbose_name_plural': 'Customers'},
        ),
        migrations.AlterModelOptions(
            name='vendoraccount',
            options={'verbose_name': 'Customer Account', 'verbose_name_plural': 'Customer Accounts'},
        ),
        migrations.AlterField(
            model_name='vendor',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Customer name'),
        ),
        migrations.AlterField(
            model_name='vendoraccount',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_accounts', to='vendors.Vendor', verbose_name='Customer'),
        ),
    ]
