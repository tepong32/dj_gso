from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
	name = models.CharField(max_length=50)

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return f"{self.name}".strip()

class SubCategory(models.Model):
	name = models.CharField(max_length=50)

	class Meta:
		verbose_name_plural = "Sub-Categories"

	def __str__(self):
		return f"{self.name}".strip()



class Asset(models.Model):
	added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # sets the user who created the instance as the "added_by" attr
	added_on = models.DateTimeField(auto_now_add=True, null=True) # automatically records the creation date of the instance
	modified_on = models.DateTimeField(auto_now=True) # when the entry gets modified, this will automatically change to the date&time the changes were saved
	date = models.DateField(verbose_name='Purchase Date', help_text="yyyy-mm-dd format")
	obrNum = models.PositiveSmallIntegerField(verbose_name="OBR #")
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True) # blank=False
	sub_category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True) # blank=False
	brand = models.CharField(max_length=100)
	supplier = models.CharField(max_length=100)
	price_per_unit = models.DecimalField(max_digits=11, decimal_places=2, help_text="from 0 to 999,999,999.99")
	qty = models.PositiveSmallIntegerField(default=1)

	working = "Working"
	not_working = "Not Working"
	turned_over = "Turned Over to GSO"
	status_choices = [
		(working, "Working"),
		(not_working, "Not Working"),
		(turned_over, "Turned Over to GSO"),
	]
	status = models.CharField(blank=True, null=False, max_length=80, choices=status_choices, default=working)
	returned_date = models.DateField(blank=True, null=True, help_text="Please do not forget to add the return-date here if the asset was surrendered to GSO")
	notes = models.TextField(blank=True)

	def __str__(self):
		return f"{self.date} | {self.obrNum} | {self.brand} | {self.supplier}"












'''
date
obr
category (furniture, machine, accessory)
brand
price
qty
notes (s/n,)
status (working, not working, returned)


'''
