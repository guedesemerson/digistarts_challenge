from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator


class Number(models.Model):
    number_array = ArrayField(models.IntegerField(
        validators=[MinValueValidator(-1000), MaxValueValidator(1000)])
    )
    result_array = ArrayField(models.IntegerField(
        validators=[MinValueValidator(-1000), MaxValueValidator(1000)]), blank=True, null=True
    )

    def __str__(self):
        return f'{self.id}'

