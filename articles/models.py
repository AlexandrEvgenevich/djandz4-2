from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Tags(models.Model):
    topic = models.CharField(max_length=50)
    tag = models.ManyToManyField(Article, through='Scopes', related_name='scopes')
    is_main = models.BooleanField(unique=True)


class Scopes(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scope')
    scope = models.ForeignKey(Tags, on_delete=models.CASCADE, related_name='scope')
