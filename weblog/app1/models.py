from django.db import models
import datetime
from datetime import timedelta
from django.contrib.gis.db import models
from django.utils import timezone



class User(models.Model):
    name = models.CharField(max_length=100,unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    imgPro = models.ImageField(blank=True,null=True)
    bio = models.CharField(max_length=1000,default="Hi there!!")
    tellegramID = models.CharField(max_length=500,blank=True,null=True)
    phone = models.CharField(max_length=500,blank=True,null=True)
    site = models.URLField(blank=True,null=True)

    date = models.DateTimeField(default=datetime.datetime.now())
    isVerified = models.BooleanField(default=False)


    def __str__ (self):
        return  "%s   %s" %(str(self.id) ,self.name)


class followers(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    another_user = models.ManyToManyField(User,related_name="another_user_followers",null=True,blank=True)

    def __str__(self):
        return  str(self.user)

class following(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    another_user = models.ManyToManyField(User,related_name="another_user_following")

    def __str__(self):
        return  str(self.user)

class Blog(models.Model):
    subject = models.CharField(max_length=500)
    text = models.TextField()
    date = models.DateTimeField(default=datetime.datetime.now())
    like = models.IntegerField(default=0)

    img = models.ImageField(upload_to ='media/img/',blank=True,null=True)
    file = models.FileField(blank=True,null=True)
    url = models.URLField(blank=True,null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (self.subject)


class Chat(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    text = models.TextField()
    like = models.IntegerField(default=0)

    def __str__(self):
        return  "%s __ %s" %(self.name,self.blog)

class Report(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return "%s __ %s __ %s" %(self.name,self.blog,self.subject)


class all_users_chat(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
    like = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return "user=(%s) | time=(%s) | id=(%s)" %(self.user,self.date,self.id  )

class all_users_chat_message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
    like = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now())
    reply = models.ForeignKey(all_users_chat,on_delete=models.CASCADE)

    def __str__(self):
        return "%s __ %s" %(self.user,self.date )
