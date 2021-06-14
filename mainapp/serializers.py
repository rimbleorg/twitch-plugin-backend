from rest_framework import serializers
from mainapp.models import BroadCastId

class BroadCastIdSerializer(serializers.ModelSerializer):
	class Meta:
		model = BroadCastId
		fields = ['access_code']

