from django.shortcuts import render



# Create your views here.

articles = [
    {'id':1, 'title' : 'First One', },
    {'id':2, 'title' : 'Second One', },
    {'id':3, 'title' : 'ETC One', },
    {'id':4, 'title' : 'Secret One', },
]



def blog_home(request):
    context = {'articles': articles}
    return render(request, 'home.html', context)


def article(request, id):
    article = None
    for i in articles:
        if i['id'] == int(id):
            article = i

    context = {'article ' : article}
    return render(request, 'article.html', context)