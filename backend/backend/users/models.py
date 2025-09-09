from django.db import models


class Staff(models.Model):
    ROLE_CHOICES=[
        ('Admin','Admin'),
        ('Cashier','Cashier'),
        ('Waiter','Waiter'),
        ('Chef','Chef'),
        ('DeliveryBoy','Delivery Boy'),
        ('Other','Other')
    ]
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    role=models.CharField(max_length=20,choices=ROLE_CHOICES)
    custom_role=models.CharField(max_length=50,null=True,blank=True)
    phone=models.CharField(max_length=15,unique=True)
    hire_date=models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[("Active", "Active"), ("Inactive", "Inactive"), ("Resigned", "Resigned")],
        default="Active"
    )
    salary=models.FloatField()
    image=models.ImageField(upload_to="staff_photos/",null=True,blank=True)

    def __str__(self):
        if self.role=="Other" and self.custom_role:
            return f"{self.name} ({self.custom_role})"
        return f"{self.name} ({self.role})"
    


class Shift(models.Model):
    shift_type=models.CharField(
        max_length=20,
        choices=[("Morning", "Morning"), ("Evening", "Evening"), ("Night", "Night"), ("Custom", "Custom")],
        default='Custom'
    )
    staff=models.ForeignKey(Staff,on_delete=models.CASCADE,related_name="shifts")
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()

    def __str__(self):
        return f"{self.staff.name} - {self.start_time} to {self.end_time}"