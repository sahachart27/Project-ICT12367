from django.db import models

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('waiting', 'รอดำเนินการ'),
        ('interviewed', 'ยืนยันแล้ว'),
        ('hired', 'ไม่ผ่านเงื่อนไข'),
        ('not_passed', 'รอชำระเงิน'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    position_applied = models.CharField(max_length=100)
    experience = models.TextField()
    application_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='waiting')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position_applied}"
