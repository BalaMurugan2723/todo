from django.db import models

# Create your models here.
from django.utils import timezone

class Todo(models.Model):
	title=models.CharField(max_length=100)
	details=models.TextField()
	date=models.DateTimeField(default=timezone.now)

	def _str_(self):
		return self.title