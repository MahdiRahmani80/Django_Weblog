from app1.models import (User,followers,following,Blog,Chat,
                         Report,all_users_chat,all_users_chat_message)
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from app1.api.serializer import (userSerilaizer,followersSerializer,followingSerializer,blogSerializer,
                chatSerializer,reportSerilalizer,all_chat_serializer,all_users_chat_message_serializer)


class userLists(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = userSerilaizer
    permission_classes = [IsAdminUser]       # how send api if this parametr is on ??

class edituser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = userSerilaizer
    lookup_field = 'id'
    permission_classes = [IsAdminUser]

class createFollowers(generics.CreateAPIView):
    queryset = followers.objects.all()
    serializer_class = followersSerializer
    permission_classes = [IsAdminUser]


class createFollowing(generics.CreateAPIView):
    queryset = following.objects.all()
    serializer_class = followingSerializer
    permission_classes = [IsAdminUser]


class  createUser (generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = userSerilaizer

class followersLists(generics.RetrieveUpdateDestroyAPIView):
    queryset = followers.objects.all()
    serializer_class = followersSerializer
    lookup_field= 'user'
    permission_classes = [IsAdminUser]       # how send api if this parametr is on ??


class followingLists(generics.RetrieveUpdateDestroyAPIView):
    queryset = following.objects.all()
    serializer_class = followingSerializer
    permission_classes = [IsAdminUser]       # how send api if this parametr is on ??
    lookup_field='user'



class CreateBlog(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = blogSerializer

class  all_blogs(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = blogSerializer

class Blog(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class =  blogSerializer
    permission_classes = [IsAdminUser]       # how send api if this parametr is on ??
    lookup_field = 'id'

class chat_create (generics.CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = chatSerializer
    permission_classes = [IsAdminUser]

class report(generics.CreateAPIView):
    queryset = Report.objects.all()
    serializer_class = reportSerilalizer

class chat (generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = chatSerializer
    lookup_field = 'blog'
    permission_classes = [IsAdminUser]

class chat_evryone (generics.CreateAPIView):
    queryset= all_users_chat.objects.all()
    serializer_class = all_chat_serializer


class message_evryone_chat_edit (generics.RetrieveUpdateDestroyAPIView):
    queryset = all_users_chat_message.objects.all()
    serializer_class = all_users_chat_message_serializer
    lookup_field = 'id'

class message_create(generics.ListCreateAPIView):
    queryset = all_users_chat_message.objects.all()
    serializer_class = all_users_chat_message_serializer
