# Generated by Django 4.2.7 on 2024-03-14 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0008_alter_leaverequest_leavestatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaverequest',
            name='Duration',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
