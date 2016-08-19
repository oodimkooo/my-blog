# coding: utf8
from django.contrib import admin
from myblog.models import BlogPost,RiderPost,MyTask,SliderPost


admin.site.register(RiderPost)
# Register your models here.

#вместо переопределения метода str основной модели можно задать отображаемые поля через админку
class PostAdmin(admin.ModelAdmin):
    list_display = ("title","shortcontent","creation_date","author")
    #Поля для поиска по объектам
    search_fields = ("author","title")

class TaskAdmin(admin.ModelAdmin):
    list_display = ("title","description","date_add","priority","author","is_completed","is_deleted")
    search_fields = ("author","title")

class SliderAdmin(admin.ModelAdmin):
    list_display = ("title","description","is_active","creation_date","get_link_to_post")
    search_fields = ["title"]

admin.site.register(BlogPost,PostAdmin)
admin.site.register(MyTask,TaskAdmin)
admin.site.register(SliderPost,SliderAdmin)

