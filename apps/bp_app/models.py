from __future__ import unicode_literals
import bcrypt#to use password encryption
from django.db import models
from datetime import date#to use datetime methods
import time#to use time.strftime methods

class UserManager(models.Manager):
    #to store methods related to User class to be used in views
    def register(self, postData):
        error_msgs = []

        try:
            if User.objects.get(username=postData['username']):
                error_msgs.append("Username already in use!")
        except:
            pass

        if len(postData['name']) < 3:
            error_msgs.append("Name is too short!")

        if len(postData['username']) < 3:
            error_msgs.append("Username is too short!")

        if len(postData['password']) < 8:
            error_msgs.append("Password is too short!")

        if not postData['password'] == postData['confirm_pw']:
            error_msgs.append("Passwords do not match!")

        if error_msgs:
            return {'errors':error_msgs}
        else:
            hashed = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            user = User.objects.create(username=postData['username'], name=postData['name'], password=hashed)
            return {'theuser':user.username, 'userid': user.id}

    def login(self, postData):
        error_msgs = []#to store error messages
        password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        #to encrypt the submitted password

        try:#to avoid erroring out our system with using ".get"(like if and else statement)
            user = User.objects.get(username=postData['username'])
            #to check if the submitted username matches the one in database
        except:#if try condition not found then use this
            error_msgs.append("Invalid user!")#to appending and sending error flash message
            return {'errors':error_msgs}#return the error in a dictionary

        if not bcrypt.hashpw(postData['password'].encode(), user.password.encode()) == user.password.encode():
            error_msgs.append("Wrong Password!")

        if error_msgs:
            return {'errors':error_msgs}
        else:
            return {'theuser':user.username, 'userid':user.id}

class User(models.Model):
    name = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


# Create your models here.
class TravelManager(models.Manager):
	def addtravel(self, postData, userid):

		error_msgs = []
		current_date = time.strftime('%Y-%m-%d')


		if len(postData['destination']) < 1:
			error_msgs.append("You need to add a destination!")
		if len(postData['description']) < 1:
			error_msgs.append("You need to add a description!")
		if len(postData['travelstart']) < 1:
			error_msgs.append("You need to add a start date!")
		if len(postData['travelend']) < 1:
			error_msgs.append("You need to add a end date!")

		if postData['travelstart'] < current_date:
			error_msgs.append("You must enter a future travel date!")
		if postData['travelend'] < postData['travelstart']:
			error_msgs.append("End date should be after start date!")

		if error_msgs:
			return {'errors':error_msgs}

		else:
			user = User.objects.get(id=userid)
			travel= Travel.objects.create(destination=postData['destination'], description=postData['description'], travelstart=postData['travelstart'],travelend=postData['travelend'],user=user)
			return {'travelid':travel.id}


class Travel(models.Model):
	join = models.ManyToManyField(User, related_name="jointravels")
	user = models.ForeignKey(User, related_name='trips')
	destination = models.CharField(max_length=255)
	description = models.TextField(max_length=500)
	travelstart = models.DateField()
	travelend = models.DateField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = TravelManager()
