from django.contrib import admin
from .models import Staff,Shift,Attendance,Payroll

admin.site.register(Staff)
admin.site.register(Shift)
admin.site.register(Attendance)
admin.site.register(Payroll)
# Register your models here.
