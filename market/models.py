from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200,db_index=True, unique=True)

	class Meta:
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('market:product_list_by_category',args=[self.slug])


class Product(models.Model):
	# general meta data about the product
	category = models.ForeignKey(Category, related_name = 'product')
	seller = models.CharField(max_length=200)

	# properties of the product
	image = models.ImageField(upload_to='product/%Y/%M/%d', blank=True)
	name = models.CharField(max_length=200,db_index=True)
	slug = models.SlugField(max_length=200, db_index=True)
	price = models.DecimalField(max_digits=10, decimal_places = 2)
	description = models.TextField(blank=True)
	reviews = models.IntegerField()

	# time of upload and update
	created = models.DateTimeField(auto_now=True)
	updated = models.DateTimeField(auto_now=True)


	class Meta:
		index_together = ('name','slug',)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('market:product_detail',args=[self.id, self.slug])





