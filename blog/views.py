from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author':'Amos Marwa',
        'title':'Blog post 1',
        'content':'First Post content',
        'date_posted':'February 15, 2021'

    },
    {
        'author':'Moronya Junior',
        'title':'Blog post 2',
        'content':'Second Post content',
        'date_posted':'February 16, 2021'

    }
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context)
def about(request):
    return render(request, 'blog/about.html', {'title':'About page'})