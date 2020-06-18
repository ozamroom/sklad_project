from django.db import models
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


class Detail_in_products(models.Model):
	detail = models.ForeignKey('List_details', on_delete = models.CASCADE, related_name='detail', blank = False, verbose_name = 'детали')
	detail_count = models.IntegerField()
	slug = models.SlugField(max_length=50, null = False, unique=True)
	
	def __str__(self):
		return 'деталь: {} кол. : {}'.format(self.detail, self.detail_count)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify('{0}{1}'.format(self.detail, self.detail_count))
		return super().save(*args, **kwargs)


class List_products(models.Model):
	title = models.CharField(max_length=50)
	count = models.IntegerField()
	slug = models.SlugField(max_length=50, null = False, unique=True)
	obj_details = models.ManyToManyField('Detail_in_products', default="default_obj_details", blank=True, verbose_name = 'детали')

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		return super().save(*args, **kwargs)

