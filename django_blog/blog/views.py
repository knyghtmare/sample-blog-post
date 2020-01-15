from django.shortcuts import render

from django.http import HttpResponse

# dummy data for testing purposes

posts = [
    {
        'author' : 'John Doe',
        'title'  : 'Blog Post 1',
        'content': 'Contents of whatever blog post this is',
        'date_posted' : 'January 16th, 2020'
    },
    {
        'author' : 'Sadia',
        'title'  : 'Blog Post 2',
        'content': 'Contents of whatever blog post this is',
        'date_posted' : 'January 17th, 2020'
    }
]


# Create your views here.
def home(request):
    context = {
        'posts' : posts
    }
    # return HttpResponse('<h1>Blog Homepage</h1>')
    return render(request, 'blog/home.html', context)


def about(request):
    # return HttpResponse("<h1>Blog About Page</h1>")
    return render(request, 'blog/about.html')
