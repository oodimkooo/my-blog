from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class quotesMain(models.Model):
    content = models.TextField(verbose_name=u"Цитата", max_length=2000)
    author = models.TextField(verbose_name=u"Автор", max_length=100)
    #publisher = models.ForeignKey(User,null=True,blank=True)
    publisher = models.TextField(verbose_name=u"Запостил", max_length=100,null=True,blank=True)
    date_published = models.DateTimeField(u'Дата публикации', auto_now_add=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        ordering = ['-date_published', ]
        verbose_name = 'цитата'
        verbose_name_plural = 'цитаты'
