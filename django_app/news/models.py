from django.db import models
from django.contrib.auth.models import User  # Импорт модели пользователя

class News_post(models.Model):
    title = models.CharField('Название новости', max_length=200)
    short_description = models.CharField('Краткое описание', max_length=200)
    text = models.TextField('Новость')
    content = models.TextField()
    pub_date = models.DateTimeField('Дата публикации')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', default=1)  # Временно сделаем поле необязательным


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
