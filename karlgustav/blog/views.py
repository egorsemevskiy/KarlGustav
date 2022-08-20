from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm  
from django.http import HttpResponse
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.models import User

# Create your views here.



def blog_home(request):
    q = request.GET.get('top-search')
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'blog/home.html', context)

def loging_page(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect("blog_home")
    if request.method == 'POST':
        username = request.POST.get('user-name')
        password = request.POST.get('user-pass')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User doesnt exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('blog_home')
        else:
            messages.error(request, 'User or Pass')

    context = {"page": page}
    return render(request, 'blog/login_regist.html', context)


def logoutUser(request):
    logout(request)
    return redirect('blog_home')


def registerUser(request):
    page = "register"
    form  = UserCreationForm()
    context = {"page": page, 'form' : form}
    return render(request, 'blog/login_regist.html', context)

def article(request, pk):
    art= Article.objects.get(id=pk)
    context = {'art': art}
    return render(request, 'blog/article.html', context)


@login_required(login_url='/login')
def createArticle(request):
    form = ArticleForm()
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_home')
    context = {'form':form}
    return render(request, 'blog/article_form.html', context)

@login_required(login_url='/login')
def updateArticle(request, pk):
    article = Article.objects.get(id = pk)
    form = ArticleForm(instance=article)
    context = {'form':form}

    if request.user != article.host:
        return HttpResponse('Not you')

    if request.method == "POST":
        form = ArticleForm(request.POST,instance=article)
        if form.is_valid():
            form.save()
            return redirect('blog_home')
    return render(request, 'blog/article_form.html', context)

@login_required(login_url='/login')
def deleteArticle(request, pk):
    article = Article.objects.get(id = pk)
    if request.method == "POST":
        article.delete()
        return redirect('blog_home')
    context = {'obj':article}
    return render(request, 'blog/delete.html', context)