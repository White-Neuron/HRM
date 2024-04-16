from django.contrib import admin
from django.http import HttpResponse
from django.conf import settings
from timesheet.models import TimeSheet,TimesheetTask
from leave.models import LeaveRequest
from leave_type.models import LeaveType
from department.models import Department
from job.models import Job
from role.models import Role
from schedule.models import Schedule,WorkShift
from .models import Employee,UserAccount
from rest_framework.authtoken.models import Token
# Custom actions
def not_allow_edit(modeladmin, request, queryset):
    settings.ALLOW_EDIT_BY_ADMIN_ONLY = True
    return HttpResponse("Chỉnh sửa không được phép.")

def export_to_txt(modeladmin, request, queryset):
    content = "\n".join([f"{field}: {getattr(obj, field)}" for obj in queryset for field in obj.__dict__])
    response = HttpResponse(content, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=exported_data.txt'
    return response

# Custom action descriptions
not_allow_edit.short_description = "Not Allow Edit"
export_to_txt.short_description = "Export selected objects to txt"

# Admin classes
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ["EmpID", "Date", "WorkShift"]

class UserAccountAdmin(admin.ModelAdmin):
    list_display = ["UserID", "EmpID"]

class TimeSheetInline(admin.TabularInline):
    model = TimeSheet

class EmployeeAdmin(admin.ModelAdmin):
    inlines = [TimeSheetInline]
    list_display = ["EmpID", "EmpName", "get_dep_name"]
    raw_id_fields = ["DepID", "JobID", "RoleID"]
    actions = [not_allow_edit]

    def get_actions(self, request):
        actions = super().get_actions(request)
        return actions

    def get_list_editable(self, request):
        if settings.ALLOW_EDIT_BY_ADMIN_ONLY and not request.user.is_superuser:
            return None
        return super().get_list_editable(request)

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if settings.ALLOW_EDIT_BY_ADMIN_ONLY and not request.user.is_superuser:
            return readonly_fields + [field.name for field in self.model._meta.fields]
        return readonly_fields

    def get_dep_name(self, obj):
        return obj.DepID.DepName if obj.DepID else ''

    get_dep_name.short_description = 'Department Name'

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["DepID", "DepName", "ManageID"]

class JobAdmin(admin.ModelAdmin):
    list_display = ["JobID", "JobName"]
    raw_id_fields = ["DepID"]

class LeaveAdmin(admin.ModelAdmin):
    list_display = ["get_name", "LeaveStatus", "LeaveTypeID", "LeaveStartDate", "LeaveEndDate", "Duration"]
    raw_id_fields = ["LeaveTypeID"]

    def get_name(self, obj):
        return obj.EmpID.EmpName if obj.EmpID else ''

    def save_model(self, request, obj, form, change):
        if obj.LeaveStartDate and obj.LeaveEndDate:
            duration = (obj.LeaveEndDate - obj.LeaveStartDate).days + 1
            obj.Duration = duration
        super().save_model(request, obj, form, change)

    get_name.short_description = 'Employee Name'

class TimeAdmin(admin.ModelAdmin):
    list_display = ["get_name", "TimeIn", "TimeOut"]
    raw_id_fields = ["EmpID"]
    actions = [export_to_txt]

    def get_name(self, obj):
        return obj.EmpID.EmpName if obj.EmpID else ''

    get_name.short_description = "Employee Name"

# Register models with admin classes
admin.site.register(Role)
admin.site.register(LeaveType)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(LeaveRequest, LeaveAdmin)
admin.site.register(TimeSheet, TimeAdmin)
admin.site.register(WorkShift)
admin.site.register(TimesheetTask)
