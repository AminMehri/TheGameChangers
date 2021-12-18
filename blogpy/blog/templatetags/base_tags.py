from django import template
from ..models import *
from django.db.models import Count, Q
from datetime import datetime, timedelta
from django.contrib.contenttypes.models import ContentType

register = template.Library()


@register.inclusion_tag("blog/partials/category_navbar.html")
def category_navbar():
    return {
        "category": Category.objects.filter(status=True)
    }


@register.inclusion_tag("blog/partials/sidebar.html")
def popular_articles():
    last_month = datetime.today() - timedelta(days=30)
    return {
        "articles": Article.objects.published().annotate(
            count=Count('hits', filter=Q(articlehit__created__gt=last_month))).order_by('-count', '-publish')[:5],
        "title": "most popular articles in last month"
    }


@register.inclusion_tag("blog/partials/sidebar.html")
def hot_articles():
    last_month = datetime.today() - timedelta(days=30)
    content_type_id = ContentType.objects.get(app_label='blog', model='article')
    return {
        "articles": Article.objects.published().annotate(
            count=Count('comments', filter=Q(comments__posted__gt=last_month) and Q(comments__content_type_id=content_type_id))
        ).order_by('-count', '-publish')[:5],
        "title": "hottest articles in last month"
    }
