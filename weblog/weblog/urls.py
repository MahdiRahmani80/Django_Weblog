from django.contrib import admin
from django.urls import path ,include
from django.conf.urls import url ,include
from django.conf import settings
from django.conf.urls.static import static
from app1.api.views import (userLists,followersLists,followingLists,Blog,createUser,CreateBlog,
                            all_blogs,chat_create,report,chat,chat_evryone,message_evryone_chat_edit,
                            message_create,edituser, createFollowers,createFollowing)
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    url(r'^users/$',userLists.as_view(),name='users'),
    url(r'^create/user/$',createUser.as_view(),name='create user'),
    url(r'^(?P<user>[0-9]+)/followers/$',followersLists.as_view(),name='followers'),  # user = 1,2,3,...
    url(r'^(?P<user>[0-9]+)/following/$',followingLists.as_view(),name='followings'), # users= 1,2,3,...
    url(r'^(?P<id>[0-9]+)/blog/$',Blog.as_view(),name='Blog'),
    url(r'^(?P<id>[0-9]+)/edit/user/$',edituser.as_view(),name='create User'),
    url(r'^create/blog/$',CreateBlog.as_view(),name='create blog'),
    url(r'^show/blogs/$',all_blogs.as_view(),name='view all blogs'),
    url(r'create/chat',chat_create.as_view(),name='create chat'),
    url(r'^report/$',report.as_view(),name='create report'),
    url(r'^(?P<blog>[0-9]+)/chat/$',chat.as_view(),name='chat'),
    url(r'^evryone/chat/$',chat_evryone.as_view(), name='chat evryone'),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]+)/evryone/messages/$',message_evryone_chat_edit.as_view(), name='message evryone'),
    url(r'^create/messages/$',message_create.as_view(), name='create'),
    url("create/followers/",createFollowers.as_view(),name='create followers'), # after make user create this part for (sent api ) and user is exist and folloing is not
    url("create/following/",createFollowing.as_view(),name='create folloing'),    # and thid , for create folloing and followers object for edit
    # Ck editor
    path('ckeditor/', include('ckeditor_uploader.urls')),


]



if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
