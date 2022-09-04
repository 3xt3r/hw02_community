from django.contrib import admin

from .models import Post, Group

class PostAdmin(admin.ModelAdmin):
    list_editable = ('group',)    
    list_display = ('pk','text', 'pub_date', 'author', 'group',)     
    search_fields = ('text',)     
    list_filter = ('pub_date',) 
    empty_value_display = '-пусто-' 

# При регистрации модели Post источником конфигурации для неё назначаем
# класс PostAdmin
admin.site.register(Post, PostAdmin)  
admin.site.register(Group)