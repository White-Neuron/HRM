# Generated by Django 4.2.7 on 2024-01-06 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_employee_bank_alter_employee_bankaccountnumer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='EmpID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.employee'),
        ),
    ]
