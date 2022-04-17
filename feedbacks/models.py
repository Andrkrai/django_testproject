from django.db import models
import catalog.models


class Feedback(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    product = models.ForeignKey(catalog.models.Product, on_delete=models.PROTECT)
    description = models.TextField()
    grade = models.PositiveSmallIntegerField()
