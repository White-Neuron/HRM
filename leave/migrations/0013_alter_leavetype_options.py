# Generated by Django 4.2.7 on 2024-06-11 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("leave", "0012_leavetype_alter_leaverequest_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="leavetype",
            options={
                "verbose_name": "Loại nghỉ phép",
                "verbose_name_plural": "Loại nghỉ phép",
            },
        ),
    ]
