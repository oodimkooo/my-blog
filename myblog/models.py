# coding: utf8
from django.db import models
from django.contrib.auth.models import User
from django_comments.moderation import CommentModerator, moderator
from taggit.managers import TaggableManager
from imagepool import models as imagepool_models


class PostCategory(models.Model):
    title = models.CharField(max_length=120,verbose_name=u"Название")
    description = models.TextField(verbose_name=u"Краткое описание",blank=True,null = False,max_length=2000)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['title']
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def get_count_of_posts_in(self):
        return BlogPost.objects.filter(category=self.id).count()

    def get_absolute_url(self):
        return "/blog/categories/%i" %self.id

class BlogPost(models.Model):
    title = models.CharField(max_length= 120)
    #background_image = models.ImageField(upload_to='blogpost/sliders/',verbose_name=u'Фон новости',blank=True,null=True)
    shortcontent = models.TextField(verbose_name=u"Краткое содержание",max_length=1000,blank=True,null=True)
    fulltext = models.TextField(verbose_name=u"Полный текст",max_length=10000,blank=True,null=True)
    creation_date = models.DateTimeField(u'Дата создания',auto_now_add=True)
    published_date = models.DateTimeField(u'Дата публикации',blank=True, null=True)
    author = models.ForeignKey(User,null=True,blank=True)
    is_commentable = models.BooleanField(default=True,verbose_name="Комментарии")  # возможность комментировать, логическое
    category = models.ForeignKey('myblog.PostCategory',null=True,blank=True)
    userUpVotes = models.ManyToManyField(User, blank=True, related_name='postUpVotes')
    userDownVotes = models.ManyToManyField(User,  blank=True, related_name='postDownVotes')
    tags = TaggableManager(blank=True,verbose_name=u'Теги')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id

    def get_post_rating(self):
        postRating = self.userUpVotes.all().count() - self.userDownVotes.all().count()
        return postRating

    class Meta:
        ordering = ['-creation_date',]
        verbose_name = 'пост'
        verbose_name_plural = 'посты'

class BlogPostModerator(CommentModerator):
    email_notification = False
    auto_close_field = 'creation_date'
    enable_field = "is_commentable"
    close_after = 7
moderator.register(BlogPost,BlogPostModerator)
