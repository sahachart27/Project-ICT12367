from django.contrib import admin
from .models import JobApplication

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position_applied', 'application_status', 'created_at')  # ✅ ตรวจสอบว่ามี created_at อยู่ในโมเดล
    search_fields = ('first_name', 'last_name', 'position_applied')
    list_filter = ('application_status', 'created_at')  # ✅ แก้ให้ใช้ฟิลด์ที่มีอยู่จริง
