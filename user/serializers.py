from rest_framework import serializers 

from .models import User, Comment, TypeLesson


class OwnerCommentSerializer(serializers.ModelSerializer):

	class Meta:
		model = User 
		fields = ['name', 'surname', 'subscription']

class LikeSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ['id']

class CommentSerializer(serializers.ModelSerializer):

	owner = OwnerCommentSerializer()

	class Meta:
		model = Comment

		fields = ['text','owner','date',]

class Userserializer(serializers.ModelSerializer):
	""" Сериализация юзеров для главной страници """
	recipient_comment = CommentSerializer(many=True, required=False)
	like = LikeSerializer(many=True, required=False)
	class Meta:
		model = User 
		depth = 2
		fields = ('id','name','surname','email','mobile_number','recipient_comment',
					'img','about','age','city','price_per_hource',
					'type_persone','skype','telegram',
					'viber','instagram','type_lesson',
					'skill','like','subscription')

class TypeSerializer(serializers.ModelSerializer):

	class Meta:
		model = TypeLesson
		fields = ('id',)

class UserProfileSerializer(serializers.ModelSerializer):
	""" Сериализация профаила юзера"""
	recipient_comment = CommentSerializer(many=True, required=False)
	type_lesson = TypeSerializer(many=True, required=False)

	class Meta:	
		model = User 
		fields = ('id', 'name', 'surname', 'email', 'mobile_number',
			'img', 'about', 'age', 'city', 'price_per_hource', 
			'type_persone', 'skype','telegram','viber','instagram',
			'type_lesson','skill','subscription', 'valid_announcement', 'like', 'recipient_comment')
		depth=2
