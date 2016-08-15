from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from PIL.ExifTags import TAGS
from io import StringIO
from os import remove

def get_exif(smth):
    data = {}
    img = Image.open(smth)
    tags = img._getexif()
    for tag, value in tags.items():
        decoded = TAGS.get(tag, tag)
        data[decoded] = value
    return data

# Create your models here.
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
    #title
    #exif
    image = models.ImageField(upload_to='imagepool/%Y/%m',verbose_name=u'Изображение',default=None)
    #meta = get_exif(image.)


    class Meta:
        ordering = ['user','-date_upload']
        verbose_name = 'изображение' #имя в админке
        verbose_name_plural = 'изображения' #имя в админке во множественном числе

    def get_absolute_url(self):
        return "/imagepool/%i/" % self.id

    def delete(self,*args,**kwargs):
        self.image.delete(save = False) #не сохранять файлы физически, удалять вместе с объектом
        super(ImagePool,self).delete(*args,**kwargs)

    def get_next(self):
        next = self.get_next_by_date_upload()
        return next.get_absolute_url()

    def get_prev(self):
        prev = self.get_previous_by_date_upload()
        return prev.get_absolute_url()

