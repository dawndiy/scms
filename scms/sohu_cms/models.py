from django.db import models

STATUS_CHOICES = (
    ('E', 'Editing'),
    ('P', 'Published'),
    ('D', 'Deleted'),
)

class Author(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)

    def __unicode__(self):
        return u'%s' % (self.name)

class Category(models.Model):
    """docstring for Tags"""
    category_name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.category_name

class Article(models.Model):
    title = models.CharField(max_length=50)
    publish_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    author = models.ForeignKey(Author)
    categorys = models.ManyToManyField(Category, blank=True)
    content = models.TextField()
    like = models.PositiveIntegerField(blank=True, default=0)
    dislike = models.PositiveIntegerField(blank=True, default=0)
    
    def __unicode__(self):
        return u'%s %s %s' % (self.title, self.author, self.publish_time)
