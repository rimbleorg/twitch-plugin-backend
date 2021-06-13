from django.shortcuts import render
from mainapp.models import BroadCastId
from mainapp.serializers import BroadCastIdSerializer
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework import status





# Create your views here.
class BroadCastIdViewSet(generics.ListCreateAPIView):
	"""
	This viewset automatically provides `list`, `create`, `retrieve`,
	`update` and `destroy` actions.

	"""
	queryset = BroadCastId.objects.all()
	serializer_class = BroadCastIdSerializer

	def create(self, request, *args, **kwargs):
		request_data = request.data
		username = request_data['username']
		broadcast_id = request_data['broadcast_id']
		access_code = request_data['access_code']

		print("Request data is {}".format(request_data))
		print("Username is {}".format(username))
		print("Broadcast id is {}".format(broadcast_id))
		print("Access code is {}".format(access_code))

		# You could call your functions that authenticates and sends the username, and broadcast id to Sehaj over here

		serializer = self.get_serializer(data=request_data)        
		serializer.is_valid(raise_exception=True)


		# self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response(
		   data={
			   "status": 201,
			   "message": "Product Successfully Created",                
			   "data": serializer.data,                
			   },
			   status=status.HTTP_201_CREATED,
			   headers=headers
		   )
