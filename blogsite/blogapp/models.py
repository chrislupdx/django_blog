from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models

class Blogpost(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=250)
	body = models.TextField()
	timestamp = models.DateTimeField(default=datetime.now())
	
	# pub_date = models.DateTimeField()


class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	blogpost = models.ForeignKey(Blogpost, on_delete=models.CASCADE, related_name='comments')
	body = models.CharField(max_length= 25000)
	timestamp= models.DateTimeField()
