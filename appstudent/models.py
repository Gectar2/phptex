from django.db import models

class Addurlstudent(models.Model):
    name_link = models.CharField(        
        'Имя ссылки',
        max_length=250,
        null=False,)
    name_page = models.CharField(        
        'Имя страницы',
        max_length=250,
        null=False,)
    content_text = models.TextField(
        'Информационный блок',
        null=False,
    )

    class Meta:
        verbose_name = ("Добавить страницу")
        verbose_name_plural = ("Добавить страницу")

    def __str__(self):
        return self.name_link
