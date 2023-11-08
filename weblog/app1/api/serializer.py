from app1.models import (User,followers,following,Blog,Chat,Report,
                         all_users_chat, all_users_chat_message)
from rest_framework import serializers


class userSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class followersSerializer(serializers.ModelSerializer):
    class Meta:
        model = followers
        fields = "__all__"


class followingSerializer(serializers.ModelSerializer):
    class Meta:
        model = following
        fields = '__all__'

class blogSerializer (serializers.ModelSerializer):
    class Meta:
        model= Blog
        fields= '__all__'

class chatSerializer (serializers.ModelSerializer):
    class Meta:
        model= Chat
        fields= '__all__'

class reportSerilalizer(serializers.ModelSerializer):
    class Meta:
        model= Report
        fields = '__all__'

class all_chat_serializer(serializers.ModelSerializer):
    class Meta:
        model = all_users_chat
        fields = '__all__'

class all_users_chat_message_serializer(serializers.ModelSerializer):
    class Meta:
        model = all_users_chat_message
        fields = '__all__'
    