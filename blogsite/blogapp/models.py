from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models

class blogpost(models.Model):
	user = models.ForeignKey('account_name', on_delete=models.CASCADE)
	title = models.CharField(max_length=250)
	body = models.CharField(max_length=25000)
	timestamp = models.DateTimeField()
	
	# pub_date = models.DateTimeField()
	# author = models.ForeignKey('poster', on_delete=models.CASCADE)
		
	
class Comment(models.Model):
	user = models.ForeignKey('user', on_delete=models.CASCADE)
	blogpost = models.ForeignKey('blogpost', on_delete=models.CASCADE)
	body = models.CharField(max_length= 25000)
	timestamp= models.DateTimeField()


class Post_list(blogpost):
	Post_title = models.OneToOneField(blogpost.title, on_delete=models.CASCADE)
	poster = models.OneToOneField(blogpost.author, on_delete=models.CASCADE)
	Post_timestamp = models.DateTimeField()

class Post_Detail(models.Model):
	# title
	# username
	# timestamp
	# body
	# comments (should have user, timestamp, comment body)
