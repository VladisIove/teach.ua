from rest_framework import serializers 

from .models import User, Comment

class CommentSerializer(serializers.ModelSerializer):


	class Meta:
		model = Comment
		depth = 1 
		fields = ['text','owner','date',]

class Userserializer(serializers.ModelSerializer):
	""" Сериализация юзеров для главной страници """
	recipient_comment = CommentSerializer(many=True)
	class Meta:
		model = User 
		depth = 2
		fields = ('id','name','surname','email','mobile_number','recipient_comment',
					'img','about','age','city','price_per_hource',
					'type_persone','skype','telegram',
					'viber','instagram','type_lesson',
					'skill','like','subscription')



class UserProfileSerializer(serializers.ModelSerializer):
	""" Сериализация профаила юзера"""
	recipient_comment = CommentSerializer(many=True)

	class Meta:	
		model = User 
		fields = ('id', 'name', 'surname', 'email', 'mobile_number',
			'img', 'about', 'age', 'city', 'price_per_hource', 
			'type_persone', 'skype','telegram','viber','instagram','subscription'
			,'type_lesson','skill','subscription', 'valid_announcement', 'like', 'recipient_comment')
		depth=2