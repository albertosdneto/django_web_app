from django.shortcuts import render
# Create your views here.

posts_list = [
    {
        'author': 'Alberto',
        'title': 'Blog Post 1',
        'content': 'Conteudo do primeiro post',
        'date_posted': 'September 28, 2019'
    },

    {
        'author': 'Jack',
        'title': 'Blog Post 2',
        'content': 'Conteudo do SEGUNDO post',
        'date_posted': 'September 28, 2019'
    }
]


def home(request):
    context = {'posts': posts_list}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
