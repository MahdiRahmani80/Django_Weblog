from django.contrib import admin
from .models import (User, Blog, Chat ,Report, followers,following,all_users_chat,
                     all_users_chat_message)

class userAdmin(admin.ModelAdmin):
    list_display = ('name','id','email','date','isVerified')

class  blogAdmin(admin.ModelAdmin):
    list_display=('subject','user','like','date')

class chatAdmin(admin.ModelAdmin):
    list_display = ('name','blog','like')

class reportAdmin(admin.ModelAdmin):
    list_display = ('subject','name','blog','date')
class all_users_chat_admin(admin.ModelAdmin):
    list_display = ('user','like','date','id')

class all_users_chat_message_admin(admin.ModelAdmin):
    list_display = ('user','like','date','id','reply')

admin.site.register(User,userAdmin)
admin.site.register(Blog,blogAdmin)
admin.site.register(Chat,chatAdmin)
admin.site.register(Report,reportAdmin)
admin.site.register(followers)
admin.site.register(following)
admin.site.register(all_users_chat,all_users_chat_admin)
admin.site.register(all_users_chat_message,all_users_chat_message_admin)
