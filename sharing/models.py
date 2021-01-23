from django.db import models
from django.conf import settings

# Create your models here.

class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="donations", on_delete=models.CASCADE)
    title= models.CharField(max_length=50, null=False)
    claimed = models.BooleanField(default=False)
    claimaint = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, default=None, on_delete=models.SET_NULL)

class Tag(models.Model):
    tag = models.CharField(null=False, max_length=50)
    item = models.ForeignKey(Item,related_name="tags", on_delete=models.CASCADE)