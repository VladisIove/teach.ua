from django.contrib import admin

from .models import User, TypeLesson, Skill, Like, Comment
# Register your models here.





class UserAdmin(admin.ModelAdmin):
	fieldsets = (
			('Main info',{
				'classes': ('wide',),
				'fields': ( ('name','surname'),
			   			  ('img', 'city', 'type_persone' ,'about', ),
			   			   ('subscription', 'start_subscription', 'end_subscription'))
				}),
			('Contact info', {
				'classes': ('collapse',),
				'fields': (('email', 'mobile_number', 'skype'),
							('telegram', 'viber', 'instagram'))
				}),
			('Other info', {
				'classes': ('collapse',),
				'fields': ('type_lesson','skill','like','comment')
				}),

				)
	list_display = ('email','name', 'surname', 'subscription', 'start_subscription', 'end_subscription')		
	list_display_links = ['email',]
	list_editable = ('subscription', 'start_subscription', 'end_subscription')

admin.site.register( User, UserAdmin)
admin.site.register(Skill)
admin.site.register(Like)
admin.site.register(Comment)