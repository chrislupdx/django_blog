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

def add_comment(request, commentid):
	# comment_item = get_object_or_404(Comment, pk=commentid)
    comment_entry = Comment(text= body, user= request.user)
    comment_entry.save()
    return redirect(reverse('blogapp:index'))

#so comment_entry is gonna be good for


# do we have the views written to take comment text and send it to be back end?
# do we have the veiws written to take the 

# @permission_required('comments.can_post') #we need to figure out what arguments this would want to take
# def add_blogpost(request):
#     blog_text = request.POST['Blogpost'] #new link, we need to figure out if we should be sending it to the blog model)
#     blog_entry = Blogpost(text=todo_text) #link
#     blot_entry.save()
#     return redirect(reverse('blogapp:index'))