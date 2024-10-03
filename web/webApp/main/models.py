from django.db import models

class Artiles(models.Model):
    name = models.CharField('Имя', max_length=50)
    contact = models.CharField('Телефон', max_length=13)
    text = models.TextField('Комментарий', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

