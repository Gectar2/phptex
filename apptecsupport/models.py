from django.db import models

# Create your models here.
class Technicalsupport(models.Model):
    name = models.CharField(
        'Имя пользователя',
        max_length=200,
        null=False,
    )
    email = models.EmailField(
        'Email',
        max_length=200,
        null=False,
    )
    messages = models.TextField(
        'Сообщение пользователя',
        null=False,
    )
    date_time = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата/Время обращения'
    )
    class Meta:
        verbose_name = ("панель обращения")
        verbose_name_plural = ("панель обращения")

    def __str__(self):
        return self.name