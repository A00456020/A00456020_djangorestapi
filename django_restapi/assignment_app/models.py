from django.db import models

# Create your models here.


class Hotels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    total_number_of_rooms = models.IntegerField()
    number_of_rooms_available = models.IntegerField()
    website_url = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
