from django.db import models
from base.models import Employee
from schedule.models import WorkShift
from datetime import time

class TimeSheet(models.Model):
    TimeIn = models.DateTimeField(null=True, blank=True)
    TimeOut = models.DateTimeField(null=True, blank=True)
    EmpID = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    Late = models.FloatField(default=0,null=True,blank=True)
    WorkHour = models.FloatField(default=0,null=True,blank=True)
    def save(self, *args, **kwargs):
        if self.TimeIn and self.TimeOut:
            timein = self.TimeIn
            timeout = self.TimeOut
            print(timein.time(),timeout.time())
            if timein.time() < time(12, 0) and timeout.time() > time(13, 30):
                work_hours =(timeout - timein).total_seconds() / 3600- 1.5  
            else:
                work_hours =(timeout - timein).total_seconds() / 3600
           
            self.WorkHour = round(work_hours, 2)

        else:
            self.WorkHour = 0

        super(TimeSheet, self).save(*args, **kwargs)