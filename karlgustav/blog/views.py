from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.



def blog_home(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'blog/home.html', context)


def article(request, pk):
    art= Article.objects.get(id=pk)
    context = {'art': art}
    return render(request, 'blog/article.html', context)

def createArticle(request):
    form = ArticleForm()
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_home')
    context = {'form':form}
    return render(request, 'blog/article_form.html', context)

def updateArticle(request, pk):
    article = Article.objects.get(id = pk)
    form = ArticleForm(instance=article)
    context = {'form':form}
    if request.method == "POST":
        form = ArticleForm(request.POST,instance=article)
        if form.is_valid():
            form.save()
            return redirect('blog_home')
    return render(request, 'blog/article_form.html', context)

def deleteArticle(request, pk):
    pass