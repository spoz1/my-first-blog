#!coding:utf8
from django.db import models
from django.utils import timezone
import sys #добавить кодировку юникод в питон
reload(sys)
sys.setdefaultencoding('utf-8')

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #ссылка на другую модель
    title = models.CharField(max_length=200) #определяем текстовое поле с ограничением на количество символов
    text = models.TextField()#oпределяется поле для неограниченно длинного текста
    created_date = models.DateTimeField(         #дата и время
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):#метод публикации для записи
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title #получим текст (строку) с заголовком записи
