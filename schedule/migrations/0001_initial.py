# Generated by Django 4.2.7 on 2024-02-27 02:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0018_alter_employee_empstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TimeBlock', models.TimeField()),
                ('DateMin', models.IntegerField(default=3)),
            ],
        ),
        migrations.CreateModel(
            name='WorkShift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WorkShiftName', models.CharField(max_length=50)),
                ('StartTime', models.TimeField()),
                ('EndTime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('ConfigSchedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.configschedule')),
                ('EmpID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.employee')),
                ('WorkShift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.workshift')),
            ],
        ),
    ]
