from django.db import models

# from django.template.defaultfilters import slugify
from pytils.translit import slugify

class List_details(models.Model):
	
	title = models.CharField(max_length=50)
	count = models.IntegerField()
	slug = models.SlugField(max_length=50, null = False, unique=True)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		return super().save(*args, **kwargs)

