# あなたが実装します（Category, Entry）
from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    
class Entry(models.Model):
    title = models.CharField(max_length=80)
    body = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="entries"
    )
    def __str__(self):
        return self.title