# coding: utf8
from django.contrib import admin
from myblog.models import BlogPost,PostCategory

#вместо переопределения метода str основной модели можно задать отображаемые поля через админку
class PostAdmin(admin.ModelAdmin):
    list_display = ("title","shortcontent","creation_date","author")
    #Поля для поиска по объектам
    search_fields = ("author","title")
    class Media:
        js=('/static/myblog/js/tiny_mce/tiny_mce.js',
            '/static/myblog/js/tiny_mce/tiny_mce_init.js')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    search_fields = ("title", "description")
    class Media:
        js = ('/static/myblog/js/tiny_mce/tiny_mce.js',
              '/static/myblog/js/tiny_mce/tiny_mce_init.js')


admin.site.register(BlogPost,PostAdmin)
admin.site.register(PostCategory,CategoryAdmin)

