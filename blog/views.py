from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'CoreyMs',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27th, 2018'
    },
    {
        'author': 'James Boyer',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28th, 2018'
    },
    {
        'author': 'Sasha Souki',
        'title': 'Blog Post 3',
        'content': 'third post content',
        'date_posted': 'August 29th, 2018'
    },
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', { 'title': 'About' })
