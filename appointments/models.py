from django.db import models

# Create your models here.


class Appointment(models.Model):

    STATUS_CHOICES = [
        ('pending','Pending'),
        ('confirmed','Confirmed'),
        ('completed','Completed')
    ]

    name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=15)

    message = models.TextField()

    preferred_date = models.DateField()

    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name