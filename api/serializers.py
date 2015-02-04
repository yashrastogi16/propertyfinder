from django.forms import widgets
from rest_framework import serializers
from feed.models import *

class propertyfinderSerializer(serializers.ModelSerializer):
	class Meta:
		model = propertyfinder
		fields = ('id','offering_type','photo')