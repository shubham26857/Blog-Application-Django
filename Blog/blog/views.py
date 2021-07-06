from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
posts  =[
    {
        'author':'Shubham Sharma',
        'title':'Blog Post 1',
        'content':'first post  content',
        'date_posted':'november 23 ,1999' 
    },
    {
        'author':'shubham Das',
        'title':'Blog Post 2',
        'content':'second post  content',
        'date_posted':'october 12 ,1999' 
    }
]

def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)


def about(request):
    return render(request,'blog/about.html',{'title':'about'})
 