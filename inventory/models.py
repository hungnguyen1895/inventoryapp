from django.db import models

# Create your models here.

#table in database
class Item(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	amount = models.IntegerField()