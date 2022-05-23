from django.db import models

DVS_CHOICES = (
    ('Бензин', 'Бензин'),
    ('Дизель', 'Дизель'),
    ('Гибрид', 'Гибрид'),
)


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Car(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name_model_car = models.CharField(max_length=100)
    type_dvs = models.CharField(max_length=20, choices=DVS_CHOICES)
    price = models.IntegerField()

    def __str__(self):
        return self.name_model_car
