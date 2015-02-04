from django.db import models
from django.utils.encoding import smart_unicode
from django.utils import timezone
from datetime import datetime

# Create your models here.
OFFERING_CHOICES = (
	('CS' , 'Commercial property for sale'),
	('CR' , 'Commercial property for rent'),
	('RS' , 'Residential property for sale'),
	('RR' , 'Residential property for rent')
)
PROPERTY_CHOICES = (
	('AP' , 'Apartment / Flat'),
	('TH', 'Townhouse'),
	('BW' , 'Bungalow'),
	('CD', 'Compound'),
	)
RENTAL_CHOICES = (
	('Y', 'Yearly'), 
	('M', 'Monthly'), 
	('W', 'Weekly'),
	('D', 'Daily'),
	)
PA_CHOICES = (
	('MR', 'Maids Room'),
	('ST', 'Study'),
	('AC', 'Central A/C & Heating'),
	('BA', 'Balcony'),
	('PG', 'Private Gard'),
	)
CA_CHOICES = (
	('CR', 'Conference room'),
	('AN', 'Available Networked'),
	('DN', 'Dining in building'),
	)
FURNISHED_CHOICES = (
	('Y', 'Yes'),
	('N', 'No'),
	('P', 'Partly'),
	)
class propertyfinder(models.Model):
	reference_number = models.CharField(unique=True,max_length=50)
	offering_type = models.CharField(max_length=50,choices=OFFERING_CHOICES)
	property_type = models.CharField(max_length=50,choices=PROPERTY_CHOICES)
	price_on_application = models.BooleanField(default=None)
	price = models.FloatField()
	service_charge = models.IntegerField()
	rental_period = models.CharField(max_length=20,choices=RENTAL_CHOICES)
	cheques = models.IntegerField(max_length=10)
	city = models.CharField(max_length=50)
	community = models.CharField(max_length=50)
	sub_community = models.CharField(max_length=50)
	property_name = models.CharField(max_length=50)
	title_en = models.CharField(max_length=50)
	title_ar = models.CharField(max_length=50)
	description_en = models.TextField()
	description_ar = models.TextField()
	private_amenities = models.CharField(max_length=30,choices=PA_CHOICES)
	commercial_amenities = models.CharField(max_length=40,choices=CA_CHOICES)
	view = models.TextField()
	plot_size = models.IntegerField()
	size = models.IntegerField()
	bedroom = models.IntegerField()
	bathroom = models.IntegerField()
	agent = models.ForeignKey('agent')
	featured = models.CharField(max_length=5)
	developer = models.CharField(max_length=50)
	build_year = models.IntegerField()
	floor = models.IntegerField()
	floors_number = models.IntegerField()
	stories = models.IntegerField()
	parking = models.IntegerField()
	furnished = models.CharField(max_length=10,choices=FURNISHED_CHOICES)
	view360 = models.URLField(max_length=300)
	photo = models.ForeignKey('photo')
	floor = models.ForeignKey('floor')
	geopoints = models.CharField(max_length=300)
	def __unicode__(self):
		return smart_unicode(self.reference_number)

class agent(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField(max_length=255)
	phone = models.CharField(max_length=20)
	photo = models.URLField(max_length=200)
	info = models.TextField()
	def __unicode__(self):
		return smart_unicode(self.name)

class photo(models.Model):
	photo = models.URLField(max_length=200)
	createdat = models.DateTimeField()
	updated = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return smart_unicode(self.photo)

class floor(models.Model):
	floor = models.URLField(max_length=200)
	createdat = models.DateTimeField()
	updated = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return smart_unicode(self.floor)



