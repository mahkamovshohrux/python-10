from django.db import models

# Create your models here.
class Models10(models.Model):
    name10 = models.CharField(max_length=40)
    lastname10 = models.CharField(max_length=20)
    data10 = models.DateField()
    def __str__(self) -> str:
        return self.name10
