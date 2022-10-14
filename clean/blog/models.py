from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class Post(models.Model):
    title = models.CharField(
        max_length=32,
        verbose_name='заголовок'
    )
    subtitle = models.CharField(
        max_length=32,
        verbose_name='подзаголовок'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='URL'
    )
    date_created = models.DateTimeField(
        default=now(),
        verbose_name='дата публикации'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='автор'
    )
    image = models.ImageField(
        upload_to='posts/',
        verbose_name='картинка'
    )
    body = models.TextField(
        verbose_name='текст'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        db_table = 'blog_posts'
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        ordering = ('date_created', )


class Contact(models.Model):
    name = models.CharField(
        max_length=24,
        verbose_name='имя'
    )
    email = models.CharField(
        max_length=24,
        verbose_name='почта'
    )
    message = models.CharField(
        max_length=256,
        verbose_name='сообщение'
    )
    date_created = models.DateTimeField(
        default=now(),
        verbose_name='дата обращения'
    )

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'blog_contacts'
        verbose_name = 'обращение'
        verbose_name_plural = 'обращения'
        ordering = ('date_created', )
