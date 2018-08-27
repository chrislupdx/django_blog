from django.shortcuts import render, redirect, get_object_or_404, reverse
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
def add_comment(request, blog_pk): #commentid
    blog = get_object_or_404(Blogpost, pk=blog_pk)
    commenttext = request.POST['comment_text']
    comment_entry = Comment(user= request.user, blogpost = blog, body = commenttext, )
    comment_entry.save()
    return redirect(reverse('blogapp:index'))
#this view passes comment info from template to models

#so comment_entry is gonna be good forblogpost


# do we have the views written to take comment text and send it to be back end?
# do we have the veiws written to take the 

@permission_required('blogpost.can_post')
def add_blogpost(request):
    if request.method == 'POST':
        blog_body = request.POST['blog_text']
        blog_title = request.POST['title']
        blog_entry = Blogpost(user = request.user, body = blog_body, title = blog_title)
        blog_entry.save()
    return redirect(reverse('blogapp:index'))
    # return redirect(reverse('blogapp:index'))