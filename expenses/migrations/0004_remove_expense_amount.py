# Generated by Django 2.2.6 on 2019-10-31 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_expenseinstallment_expense'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='amount',
        ),
    ]
