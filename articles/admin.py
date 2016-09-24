from django.contrib import admin
from django.utils.safestring import mark_safe

from articles.models import Article, Category


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date', 'small_text',)
    list_filter = ('categories',)
    search_fields = ('title', 'author__username', 'text', 'small_text')
    readonly_fields = ('creation_date', 'modification_date')

    fieldsets = (
        ("Title and description", {
            'fields': ('title', 'small_text', 'text'),
            'classes': ('wide',)
        }),
        ('Author', {
            'fields': ('author',),
            'classes': ('wide',)
        }),
        ('URL', {
            'fields': ('url',),
            'classes': ('wide',)
        }),
        ('Categories', {
            'fields': ('categories',),
            'classes': ('wide', 'collapse')
        }),
        ('Date', {
            'fields': ('publication_date', 'creation_date', 'modification_date'),
            'classes': ('wide',)
        })
    )

    def image_tag(self, article):
        return mark_safe("<img src={0}>".format(article.url))


# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
