from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    title       = models.CharField('TITLE', max_length=50)
    slug        = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, null=True, help_text='Request detail.')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)
    content = models.TextField('CONTENT')
   
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'my_posts'
        ordering = ('-modify_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('individual:post_detail', args=(self.slug,))

    # def get_previous_post(self):
    #     return self.get_previous_by_modify_date()

    # def get_next_post(self):
    #     return self.get_next_by_modify_date()

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.slug = slugify(self.title, allow_unicode=True)

        # super(Post, self).save(*args, **kwargs)


class Individual(models.Model):
    user_name = models.CharField('USER_NAME', max_length = 50)
    enterprise_name = models.CharField('ENTERPRISE_NAME', max_length = 50)
    additional = models.TextField('ADDITIONAL')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    Modify_date = models.DateTimeField('Modify Date', auto_now= True)
    owner = models.ForeignKey(User, null= True, on_delete=models.CASCADE)

    def get_next_post(self):
        return self.get_next_by_modify_date()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title, allow_unicode= True)
        super(Individual,self).save(*args, **kwargs)