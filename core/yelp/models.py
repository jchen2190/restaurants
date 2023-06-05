from django.db import models
from django.urls import reverse

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200, null=True, blank=True)
    address3 = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    image_url = models.URLField(max_length=200, blank=True)
    category = models.CharField(max_length=100)
    review_count = models.IntegerField(null=True, blank=True)
    price = models.CharField(max_length=10, blank=True)
    rating = models.FloatField()
    phone = models.CharField(max_length=20, blank=True)
    tag = models.ManyToManyField('Tag', blank=True, default="good")

    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse("posts-detail", kwargs={"pk":self.id})
    
class Tag(models.Model):
    tag_field = models.CharField(max_length = 200, blank=False)

    def __str__(self):
        return str(self.tag_field)