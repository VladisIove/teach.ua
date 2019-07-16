from rest_framework import serializers 

from .models import User, Comment

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment 
		fields = ['id','text','recipient','owner','date',]

class Userserializer(serializers.ModelSerializer):
	""" Сериализация юзеров для главной страници """
	recipient_comment = CommentSerializer(many=True)
	class Meta:
		model = User 
		depth = 1
		fields = ('id','name','surname','email','mobile_number','recipient_comment',
					'img','about','age','city','price_per_hource',
					'type_persone','skype','telegram',
					'viber','instagram','type_lesson',
					'skill','like','subscription')