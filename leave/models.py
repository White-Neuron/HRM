from django.db import models
from base.models import Employee
from datetime import datetime
from leave_type.models import LeaveType
from datetime import time
# Create your models here.
class LeaveRequest(models.Model):
    LeaveRequestID = models.AutoField(primary_key=True)
    EmpID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    LeaveStartDate = models.DateTimeField()
    LeaveEndDate = models.DateTimeField()
    # LeaveStartHour = models.TimeField(default=time(8, 0))
    # LeaveEndHour = models.TimeField(default=time(17, 30))
    LeaveTypeID = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    Reason = models.CharField(max_length=500)
    STATUS_CHOICES = [
        ('Chờ xác nhận', 'Chờ xác nhận'),
        ('Chờ phê duyệt', 'Chờ phê duyệt'),
        ('Đã phê duyệt', 'Đã phê duyệt'),
        ('Đã từ chối', 'Đã từ chối'),
    ]

    LeaveStatus = models.CharField(
        max_length=255,
        choices=STATUS_CHOICES,
        default='Chờ xác nhận',
    )
    Duration=models.IntegerField(null=True,blank=True)
    
    def save(self, *args, **kwargs):
        if self.LeaveStartDate and self.LeaveEndDate:
            start_date = self.LeaveStartDate
            end_date = self.LeaveEndDate
            
            self.Duration = (end_date - start_date).days + 1
        else:
            self.Duration = 0
        
        super(LeaveRequest, self).save(*args, **kwargs)

        
