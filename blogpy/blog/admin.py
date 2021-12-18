from django.contrib import admin
from .models import *


def make_published(modeladmin, request, queryset):
    rows_updated = queryset.update(status='p')
    if rows_updated == 1:
        message_bit = "1 story was"
    else:
        message_bit = "%s stories were" % rows_updated
    modeladmin.message_user(request, "%s successfully marked as published." % message_bit)
make_published.short_description = "Mark selected stories as published"


def make_draft(modeladmin, request, queryset):
    rows_updated = queryset.update(status='d')
    if rows_updated == 1:
        message_bit = "1 story was"
    else:
        message_bit = "%s stories were" % rows_updated
    modeladmin.message_user(request, "%s successfully marked as draft." % message_bit)
make_draft.short_description = "Mark selected stories as draft"


def make_status_true(modeladmin, request, queryset):
    rows_updated = queryset.update(status=True)
    if rows_updated == 1:
        message_bit = "1 Category was"
    else:
        message_bit = "%s Categorys were" % rows_updated
    modeladmin.message_user(request, "%s successfully marked as Status True." % message_bit)
make_status_true.short_description = "Mark selected Categorys as Status True"


def make_status_false(modeladmin, request, queryset):
    rows_updated = queryset.update(status=False)
    if rows_updated == 1:
        message_bit = "1 Category was"
    else:
        message_bit = "%s Categorys were" % rows_updated
    modeladmin.message_user(request, "%s successfully marked as Status False." % message_bit)
make_status_false.short_description = "Mark selected Categorys as Status False"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {"slug": ('title',)}
    actions = [make_status_true, make_status_false]


admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_picture', 'slug', 'author', 'publish', 'is_special', 'status', 'category_to_str')
    list_filter = ('publish', 'status', 'author')
    search_fields = ('title', 'description')
    prepopulated_fields = {"slug": ('title',)}
    actions = [make_published, make_draft]

    def category_to_str(self, obj):
        return ", ".join([category.title for category in obj.category_published()])
    category_to_str.short_description = "Category"


admin.site.register(Article, ArticleAdmin)
admin.site.register(IPAddress)
