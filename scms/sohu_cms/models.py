# -*- coding: utf-8 -*-
from django.db import models

STATUS_CHOICES = (
    ('E', '编辑中'),
    ('P', '已发布'),
    ('D', '已删除'),
)

class Tag(models.Model):
    '''标签模型'''
    tag_name = models.CharField(max_length=20, verbose_name='标签名')

    def __unicode__(self):
        return self.tag_name
    
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签列表'

class Article(models.Model):
    '''新闻文章模型'''
    title = models.CharField(max_length=50, verbose_name='标题')
    publish_time = models.DateTimeField(auto_now_add=True, verbose_name='时间')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name='状态')
    author = models.ForeignKey('auth.User', verbose_name='作者')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')
    content = models.TextField(verbose_name='内容')
    like = models.PositiveIntegerField(blank=True, default=0,  verbose_name='顶')
    dislike = models.PositiveIntegerField(blank=True, default=0, verbose_name='踩')
    
    def __unicode__(self):
        return u'%s %s %s' % (self.title, self.author, self.publish_time)
        
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章列表'
        ordering = ['-publish_time']
