from django.contrib import admin
from .models import ImagePool,ImageAlbum


class ImagePoolAdmin(admin.ModelAdmin):
    list_display = ("title","albumId","user","date_upload","is_commentable")
    search_fields = ("user","title")

class ImageAlbumAdmin(admin.ModelAdmin):
    list_display = ("title","shortdescription","user","date_created")
    search_fields = ("user","title")

admin.site.register(ImagePool,ImagePoolAdmin)
admin.site.register(ImageAlbum,ImageAlbumAdmin)
