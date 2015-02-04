from django.shortcuts import render
from serializers import *
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from feed.models import *
import collections
from collections import defaultdict

@api_view(['GET','POST'])
def feed(request):
	try:
		dub = propertyfinder.objects.all()
	except dub.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	if request.method == 'GET':
		prop = []
		for i in dub:
			agent1 = []
			data1 = collections.OrderedDict()
			data = collections.OrderedDict()
			agent = collections.OrderedDict()
			data['reference_number'] = i.reference_number
			print data['reference_number']
			data['offering_type'] = i.offering_type
			data['property_type'] = i.property_type
			data['price_on_application'] = i.price_on_application
			data['price'] = i.price
			data['service_charge'] = i.service_charge
			data['rental_period'] = i.rental_period
			data['cheques'] = i.cheques
			data['city'] = i.city
			data['community'] = i.community
			data['sub_community'] = i.sub_community
			data['property_name'] = i.property_name
			data['title_en'] = i.title_en
			data['title_ar'] = i.title_ar
			data['description_en'] = i.description_en
			data['description_ar'] = i.description_ar
			data['private_amenities'] = i.private_amenities
			data['commercial_amenities'] = i.commercial_amenities
			data['view'] = i.view
			data['plot_size'] = i.plot_size
			data['size'] = i.size
			data['bedroom'] = i.bedroom
			data['bathroom'] = i.bathroom
			agent['name'] = i.agent.name
			agent['email'] = i.agent.email
			agent['phone'] = i.agent.phone
			agent['photo'] = i.agent.photo
			agent['info'] = i.agent.info
			agent1.append(agent)
			data['agent'] = agent1
			data['featured'] = i.featured
			data['developer'] = i.developer
			data['build_year'] = i.build_year
			data['floor'] = str(i.floor)
			data1['property'] = data 
			prop.append(data1)
		return Response(prop)