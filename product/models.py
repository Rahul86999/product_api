from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

class ProductCateogry(models.Model):
	name_category = models.CharField(_('Product Category'),max_length=250,null=True,blank=True)
	
	def __str__(self):
		return str(self.name_category)

class Product(models.Model):
    product_category = models.ForeignKey(ProductCateogry, on_delete=models.CASCADE)
    product_name = models.CharField(_('Product Name'),max_length=250,null=True,blank=True)
    product_image = models.ImageField(upload_to="product_images/",null=True,blank=True)
    color = models.CharField(_('Color'),max_length=250,null=True,blank=True)
    price = models.FloatField(_('Price'),blank=True, null=True)

    def __str__(self):
        return str(self.product_name)
