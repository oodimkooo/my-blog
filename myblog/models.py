# coding: utf8
from django.db import models
from django.contrib.auth.models import User
from django_comments.moderation import CommentModerator, moderator
from taggit.managers import TaggableManager
from precise_bbcode.fields import BBCodeTextField
from redactor.fields import RedactorField
from imagepool import models as imagepool_models


class BlogPost(models.Model):
    title = models.CharField(max_length= 120)
    #on_slider = models.BooleanField(default=False,verbose_name=u'На слайдере?')
    #main_slide = models.BooleanField(default=False,verbose_name=u'Основной слайд?')
    #background_image = models.ImageField(upload_to='blogpost/sliders/',verbose_name=u'Фон новости',blank=True,null=True)
    #shortcontent = models.TextField(verbose_name=u"Краткое содержание",max_length=1000,blank=True,null=True)
    shortcontent = RedactorField(verbose_name=u"Краткое содержание",max_length=1000,blank=True,null=True)
    #fulltext = models.TextField(verbose_name=u"Полный текст",max_length=10000,blank=True,null=True)
    fulltext = RedactorField(verbose_name=u"Полный текст",max_length=10000,blank=True,null=True)
    creation_date = models.DateTimeField(u'Дата создания',auto_now_add=True)
    published_date = models.DateTimeField(u'Дата публикации',blank=True, null=True)
    # отношение один ко многим, возможно стоит добавить on_delete=models.CASCADE
    author = models.ForeignKey(User,null=True,blank=True)
    is_commentable = models.BooleanField(default=True,verbose_name="Комментарии")  # возможность комментировать, логическое
    # related_name - поле для работы со связанным объектом - User
    # По привычке задавал null= True, но получал ворнинг, т.к. "null has no effect since there is no way to require a relationship at the database level."
    userUpVotes = models.ManyToManyField(User, blank=True, related_name='postUpVotes')
    userDownVotes = models.ManyToManyField(User,  blank=True, related_name='postDownVotes')

    #tags - теги через модуль django-taggit-0.20.1
    tags = TaggableManager(blank=True,verbose_name=u'Теги')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id

    #метаданные модели, дополнительные параметры для кастомизации вида или поведения
    class Meta:
        ordering = ['-creation_date',] #союственно сортировка на страницк
        verbose_name = 'пост' #имя в админке
        verbose_name_plural = "посты" #имя в админке во множественном числе


# Автомодератор, стандартный функционал модуля comments
class BlogPostModerator(CommentModerator):
    email_notification = False
    auto_close_field = 'creation_date'
    enable_field = "is_commentable"
    close_after = 7
moderator.register(BlogPost,BlogPostModerator)

#На время разработки

class MyTask(models.Model):
    title = models.CharField(max_length=120,verbose_name=u'Задача')
    description = models.TextField(verbose_name=u'Краткое описание',max_length=5000,blank=True,null=True)
    date_add = models.DateTimeField(verbose_name=u'Дата добавления',auto_now_add=True)
    priority = models.IntegerField(verbose_name=u'Приоритет задачи',blank=True,null=True)
    author = models.ForeignKey(User,null=True,blank=True)
    is_completed = models.BooleanField(default=False,verbose_name="Выполнено?")
    is_deleted = models.BooleanField(default=False,verbose_name="Отменено?")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/tasks/%i/"%self.id

    class Meta:
        ordering=['priority']
        verbose_name = 'задача'
        verbose_name_plural = "задачи"

#Для участников команды - собственно те же посты, но в отдельном каталоге с рядом специфичных полей (о себе, возраст, бла бла бла)

class RiderPost(models.Model):
    name = models.CharField(max_length=120,verbose_name=u"ФИО")
    shortinfo = models.TextField(verbose_name=u"О себе",max_length=5000,null=True,blank=True)
    #foto_path
    #user_fun_groups

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/team/%i/" % self.id

#Для анонсов в слайдере
class SliderPost(models.Model):
    title = models.CharField(max_length=120,verbose_name=u"Заголовок")
    description = models.TextField(verbose_name=u'Краткое описание',max_length=1000,blank=True,null=True)
    main_post = models.ForeignKey(BlogPost, null=True, blank=True)
    is_active = models.BooleanField(default=False,verbose_name=u'Заглавный слайд?')
    creation_date = models.DateTimeField(u'Дата создания', auto_now_add=True)

    image_link = models.ForeignKey(imagepool_models.ImagePool,blank=True,null=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-creation_date', ]  # союственно сортировка на страницк
        verbose_name = 'пост в слайдере'  # имя в админке
        verbose_name_plural = "посты в слайдере"  # имя в админке во множественном числе

    def get_link_to_post(self):
        if self.main_post:
            return "/blog/%i/" % self.main_post.id
        else:
            return "None"

    def get_pos_in_object_list(self):
        return SliderPost.objects.filter(id__gt=self.id).count() + 1

    def get_image_link(self):
        if self.image_link:
            #return '/imagepool/static' + self.image_link.get_absolute_url() + self.image_link.title
            return self.image_link.image.url


