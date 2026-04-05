from django.db import models

# Create your models here.


class Testimonial(models.Model):

    patient_name = models.CharField(max_length=100)

    review = models.TextField()

    rating = models.IntegerField()

    photo = models.ImageField(upload_to="testimonials/")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient_name