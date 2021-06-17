from django.shortcuts import render
from mainapp.models import BroadCastId
from mainapp.serializers import BroadCastIdSerializer
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework import status
import json
import boto3
import requests





# Create your views here.
class BroadCastIdViewSet(generics.ListCreateAPIView):
	"""
	This viewset automatically provides `list`, `create`, `retrieve`,
	`update` and `destroy` actions.

	"""
	queryset = BroadCastId.objects.all()
	serializer_class = BroadCastIdSerializer
	
	def find_free_server(self, jsonfiles):
		for i in range(len(jsonfiles)):
			print(type(jsonfiles[i]["in_use"]), jsonfiles[i]["in_use"], len(jsonfiles))
			if(not jsonfiles[i]["in_use"]):
				return jsonfiles[i]['server_id']
		return None
	def edit_fields(self, jsonfiles, user, broadcast_id, access_token,s3_client):
		s_id = self.find_free_server(jsonfiles)
		print(s_id)
		if(s_id != None):
			jsonfiles[s_id]['in_use'] = True
			jsonfiles[s_id]['stream_url'] = "https://www.twitch.tv/" + user
			jsonfiles[s_id]['stream_type'] = "stream"
			jsonfiles[s_id]['prediction_ids'] = {}
			jsonfiles[s_id]['broadcast_id'] = broadcast_id
			jsonfiles[s_id]['access_token'] = access_token
			jsonString = json.dumps(jsonfiles)
			jsonFile = open("instructions.json", "w")
			jsonFile.write(jsonString)
			jsonFile.close()
			file_location_on_computer = './instructions.json'
			s3_client.upload_file(file_location_on_computer, 'twitch-polls-data', 'instructions.json')
		else:
			
			return None
	def get_id_and_user(self, authorization):
		url = 'https://api.twitch.tv/helix/users'
		headers={'Authorization': 'Bearer ' + authorization, 'Client-Id': '92h2m4t1t7vtoewujwz0z8xfq55qdm'}
		r = requests.get(url, headers=headers)
		return authorization, r.json()['data'][0]['id'], r.json()['data'][0]['display_name']

	def get_access_token(self, code):
		clientid = "92h2m4t1t7vtoewujwz0z8xfq55qdm"
		clientsecret = "tofgqnlvv0k96r6sq8gzmeitu7tacz"
		resp = requests.post('https://id.twitch.tv/oauth2/token?client_id=92h2m4t1t7vtoewujwz0z8xfq55qdm&client_secret=u4lmk5v25eqvjr8wqpt6wdx5cb4w0p&code='+code+'&grant_type=authorization_code&redirect_uri=http://localhost:3000')
		access_token = resp.json()["access_token"]
		return access_token

	def create(self, request, *args, **kwargs):
		request_data = request.data
		access_code = str(request_data['access_code'])
		current_session  = boto3.Session(
			aws_access_key_id='AKIAVR437LUMGQWOEEF4',
			aws_secret_access_key='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'
		)
	
		s3_client = current_session.client('s3') 
		first_object_data = s3_client.get_object(Bucket='twitch-polls-data', Key="instructions.json")
		
		user_fields = self.get_id_and_user(self.get_access_token(access_code))
		jsonfile = json.loads(first_object_data['Body'].read())
		# print(self.find_free_server(jsonfile))
		self.edit_fields(jsonfile, user_fields[2],user_fields[1],user_fields[0], s3_client)

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
