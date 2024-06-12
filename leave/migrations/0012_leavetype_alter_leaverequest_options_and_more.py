# Generated by Django 4.2.7 on 2024-06-11 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0022_alter_employee_taxcode"),
        ("leave_type", "0005_alter_leavetype_options_and_more"),
        ("leave", "0011_remove_leaverequest_leaveendhour_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="LeaveType",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("leave_type.leavetype",),
        ),
        migrations.AlterModelOptions(
            name="leaverequest",
            options={
                "ordering": ["LeaveRequestID"],
                "verbose_name": "Đơn xin nghỉ phép",
                "verbose_name_plural": "Đơn xin nghỉ phép",
            },
        ),
        migrations.AlterField(
            model_name="leaverequest",
            name="Duration",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Số ngày nghỉ"
            ),
        ),
        migrations.AlterField(
            model_name="leaverequest",
            name="EmpID",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="base.employee",
                verbose_name="Nhân viên",
            ),
        ),
        migrations.AlterField(
            model_name="leaverequest",
            name="LeaveEndDate",
            field=models.DateTimeField(verbose_name="Ngày kết thúc"),
        ),
        migrations.AlterField(
            model_name="leaverequest",
            name="LeaveRequestID",
            field=models.AutoField(
                primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="leaverequest",
            name="LeaveStartDate",
            field=models.DateTimeField(verbose_name="Ngày bắt đầu"),
        ),
        migrations.AlterField(
            model_name="leaverequest",
            name="LeaveStatus",
            field=models.CharField(
                choices=[
                    ("Chờ xác nhận", "Chờ xác nhận"),
                    ("Chờ phê duyệt", "Chờ phê duyệt"),
                    ("Đã phê duyệt", "Đã phê duyệt"),
                    ("Đã từ chối", "Đã từ chối"),
                ],
                default="Chờ xác nhận",
                max_length=255,
                verbose_name="Trạng thái",
            ),
        ),
        migrations.AlterField(
            model_name="leaverequest",
            name="LeaveTypeID",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="leave_type.leavetype",
                verbose_name="Loại nghỉ phép",
            ),
        ),
        migrations.AlterField(
            model_name="leaverequest",
            name="Reason",
            field=models.CharField(max_length=500, verbose_name="Lý do"),
        ),
    ]