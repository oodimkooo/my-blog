from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from PIL.ExifTags import TAGS
from io import StringIO
from os import remove
from django_comments.moderation import CommentModerator, moderator

import exifread

class ImageAlbum(models.Model):
    user = models.ForeignKey(User)
    date_created = models.DateTimeField(verbose_name=u'Дата создания',auto_now_add=True)
    title = models.CharField(max_length= 120,null=True,blank=True)
    shortdescription = models.CharField(max_length=1000,verbose_name=u'Краткое описание',default=None)

    class Meta:
        ordering=['-date_created']
        verbose_name = 'альбом'
        verbose_name_plural = 'альбомы'

    def get_cover(self):
        if self.imagepool_set.filter(is_cover = True).count() > 0:
            return self.imagepool_set.filter(is_cover = True)[0]
        elif self.imagepool_set.all().count() > 0:
            return self.imagepool_set.all()[0]
        else:
            return None


class ImagePool(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=120,null=True,blank=True)
    date_upload = models.DateTimeField(verbose_name=u'Дата загрузки',auto_now_add=True)
    albumId = models.ForeignKey(ImageAlbum,null=True,blank=True)
    is_cover=models.BooleanField(default=False,verbose_name="Обложка альбома?")
    image = models.ImageField(upload_to='imagepool/%Y/%m',verbose_name=u'Изображение',default=None)
    #is_commentable = models.BooleanField(default=True, verbose_name=u"Комментарии")

    class Meta:
        ordering = ['user','-date_upload']
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'

    def get_absolute_url(self):
        return "/imagepool/%i/" % self.id

    def get_exif(self,file=None):
        try:
            if file:
                tags = exifread.process_file(file)
            else:
                with self.image.storage.open(self.image.name, 'rb') as file:
                    tags = exifread.process_file(file, details=False)
            return tags
        except:
            return {}

    def delete(self,*args,**kwargs):
        self.image.delete(save = False) #не сохранять файлы физически, удалять вместе с объектом
        super(ImagePool,self).delete(*args,**kwargs)

    def get_next(self):
        next = self.get_next_by_date_upload()
        return next.get_absolute_url()

    def get_prev(self):
        prev = self.get_previous_by_date_upload()
        return prev.get_absolute_url()

class ImagePoolModerator(CommentModerator):
    email_notification = False
    auto_close_field = 'date_upload'
    enable_field = "is_commentable"
    close_after = 7
moderator.register(ImagePool,ImagePoolModerator)