from rest_framework import serializers 

from .models import User 


class Userserializer(serializers.ModelSerializer):
	""" Сериализация юзеров для главной страници """

	class Meta:
		model = User 
		fields = ('id','name','surname','email','mobile_number',
					'img','about','age','city','price_per_hource',
					'type_persone','skype','telegram',
					'viber','instagram','type_lesson',
					'skill','like','subscription')