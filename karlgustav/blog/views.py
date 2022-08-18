from django.shortcuts import render



# Create your views here.

articles = [
    {'id':1, 'title' : 'First One', },
    {'id':2, 'title' : 'Second One', },
    {'id':3, 'title' : 'ETC One', },
    {'id':4, 'title' : 'Secret One', },
]



def blog_home(request):
    return render(request, 'home.html', {'articles': articles})

def article(request):
    return render(request, 'aricle.html')