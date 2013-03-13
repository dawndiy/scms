# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from djangomako.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from models import Article, Tag
import markdown

def article_list(request):
    '''最新文章列表'''
    article_list = Paginator(Article.objects.all(), 10)     # 默认10页
    page = 1
    try:
        page = request.GET.get('page')
        articles = article_list.page(page)
    except (PageNotAnInteger, EmptyPage):
        articles = article_list.page(1)     # 不存在返回第一页
    return render_to_response('article_list.html', {'articles': articles})
    
def article_detail(request, id):
    '''文章详情'''
    article = get_object_or_404(Article, pk=id, status='P')
    article.content = markdown.markdown(article.content)
    return render_to_response('article_detail.html', {'article': article})
    
def article_digg(request, id, digg):
    '''推荐处理'''
    article = get_object_or_404(Article, pk=id, status='P')
    if digg == 'like':          # 顶一下
        article.like += 1
    elif digg == 'dislike':     # 踩一下
        article.dislike += 1
    article.save()              # 保存
    return HttpResponse()
    

def article_taglist(request, tag_name='all'):
    '''文章分类'''
    if tag_name == 'all':
        articles = Article.objects.all()
    else:
        tag = get_object_or_404(Tag, tag_name=tag_name)
        articles = Article.objects.filter(tags=tag)
    tags = Tag.objects.all()
    
    article_list = Paginator(articles, 10)
    page = 1
    try:
        page = request.GET.get('page')
        articles = article_list.page(page)
    except (PageNotAnInteger, EmptyPage):
        articles = article_list.page(1)
    
    return render_to_response('article_taglist.html', {'tags': tags, 'articles': articles, 'tag_name': tag_name})

def about(request):
    return render_to_response('about.html',{})


