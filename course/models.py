from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=128)
    start_date = models.DateField()
    description = models.CharField(max_length=1028)

    def __str__(self):
        return self.name
