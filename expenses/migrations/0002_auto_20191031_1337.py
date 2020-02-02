# Generated by Django 2.2.6 on 2019-10-31 08:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseInstallment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.IntegerField(blank=True, null=True, verbose_name='Amount Paid')),
                ('date', models.DateField(verbose_name='Date')),
                ('next_pay_date', models.DateField(verbose_name='Next Pay Date')),
            ],
            options={
                'verbose_name': 'ExpenseInstallment',
                'verbose_name_plural': 'ExpenseInstallments',
            },
        ),
        migrations.RemoveField(
            model_name='expense',
            name='date',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='next_pay_date',
        ),
        migrations.AddField(
            model_name='expense',
            name='amount',
            field=models.IntegerField(default=0, verbose_name='Amount Paid'),
            preserve_default=False,
        ),
    ]
