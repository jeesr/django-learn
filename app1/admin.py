from django.contrib import admin
from .models import Article,Person,Tag
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'score', 'author','publishTime')
    search_fields = ('title', 'author',)
    list_filter = ('author__name','author__age','author',)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('id','name','age')
    search_fields = ('name', 'age',)

admin.site.register(Article,ArticleAdmin)
admin.site.register(Person,PersonAdmin)
admin.site.register(Tag)