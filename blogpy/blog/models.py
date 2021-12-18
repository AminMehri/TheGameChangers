from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from account.models import User
from django.utils.html import format_html
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment


class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField()


class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')


class Category(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    slug = models.SlugField(max_length=128, null=False, blank=False)
    status = models.BooleanField(default=False)
    position = models.IntegerField()

    def __str__(self):
        return self.title


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('i', 'Investigation'),
        ('b', 'Back'),
    )
    title = models.CharField(max_length=128, null=False, blank=False)
    slug = models.SlugField(max_length=128, null=False, blank=False)
    category = models.ManyToManyField(Category, related_name="articles")
    description = models.TextField(null=False, blank=False)
    thumbnail = models.FileField(upload_to='images')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="articles")
    is_special = models.BooleanField(default=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    super_user_description = models.TextField(null=True, blank=True)
    comments = GenericRelation(Comment)
    hits = models.ManyToManyField(IPAddress, through="ArticleHit", blank=True, related_name='hits')

    class Meta:
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("account:home")

    def category_published(self):
        return self.category.filter(status=True)

    def thumbnail_picture(self):
        return format_html("<img width=150 height=100 style='border-radius: 5px;' src='{}'>".format(self.thumbnail.url))

    objects = ArticleManager()


class ArticleHit(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    ip_address = models.ForeignKey(IPAddress, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
