from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Blogpost, Comment
from django.contrib.auth.decorators import permission_required

def index(request):
	blogpost_list = Blogpost.objects.all()
	comments = Comment.objects.all()
	return render(request,'blogapp/index.html', {'blogposts':blogpost_list, 'comment':comments})

#we need to figure out where the incoming text is from if this is a pure "put thing is a pure post command
#whelp we just made a fuckton of new links on this page
@permission_required('comments.can_post')
def add(request):
    blog_text = request.POST['Blogpost'] #new link, we need to figure out if we should be sending it to the blog model)
    blog_entry = Todo(text=todo_text) #link
    blot_entry.save()
    return redirect(reverse('blogapp:index'))
