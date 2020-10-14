from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http  import HttpResponse
import datetime as dt
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import *
from .forms import *
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout

def all_news(request):
    all_news = Article.objects.all()
    context = {'all_news':all_news}
    return render(request, 'all-news/all_news.html',context)

def news_today(request):
    date = dt.date.today()
    news = Article.todays_news()
    
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('news_today')
    else:
        form = NewsLetterForm()
    return render(request, 'all-news/today-news.html', {"date": date,"news":news,"letterForm":form, 'all_news':all_news})


def convert_dates(dates):
    day_number = dt.date.weekday(dates)
    
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]
    
    day = days[day_number]
    return day

def past_days_news(request,date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(date,'%Y-%m-%d').date()
         
    except ValueError:
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_today)
    
    news = Article.todays_news()
    return render(request, 'all-news/past-news.html', {"date": date,"news":news})

def search_results(request):
    
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})

@login_required(login_url='/accounts/login/')   
def article(request,article_id):
    try:
        article = Article.objects.get(id = article_id)
    except ValueError:
        raise Http404()
    return render(request,"all-news/article.html", {"article":article})

@login_required(login_url='/accounts/login/')
def new_article(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.editor = current_user
            article.save()
        return redirect('/')

    else:
        form = NewArticleForm()
    return render(request, 'new_article.html', {"form": form})

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(request,'/')
    
    return render(request, '/django_registration/login.html')
        
@login_required
def logout(request):
    django_logout(request)
    return  HttpResponseRedirect('/accounts/login')
    
    
