from django.db import models
from django.utils.html import mark_safe

# Create your models here.

class Book(models.Model):
    title = models.CharField(db_column='title', max_length=100, blank=False)
    description = models.TextField(db_column='description', max_length=1000, blank=False)
    author = models.CharField(db_column='author', max_length=100, blank=False)
    year = models.IntegerField(db_column='year',blank=False, default=2000)
    image = models.ImageField(upload_to='images/')

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="95" height="70" />' % (self.image))

    image_tag.short_description = 'Image'
    
    def __str__(self) -> str:
        return self.title
