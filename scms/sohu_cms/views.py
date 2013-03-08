from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import Article

def article_list(request):
    articles = Article.objects.all()
    return render_to_response('article_list.html', {'articles': articles})
    
