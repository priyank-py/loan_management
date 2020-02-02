# Generated by Django 2.2.6 on 2019-11-05 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='account_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Account Name'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='account_number',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Account Number'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='bank_branch',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Bank Branch'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='ifsc_code',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='IFSC code'),
        ),
    ]
