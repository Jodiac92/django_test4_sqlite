from django.contrib import admin
from mydb.models import Article

# Register your models here.
#admin.site.register(Article) #db만들기, 밑에처럼~(보이도록)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'price', 'pub_date')
    
admin.site.register(Article, ArticleAdmin)