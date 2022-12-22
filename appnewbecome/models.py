from django.db import models

class Addnews(models.Model):
    title = models.CharField(
        'Название',
        max_length=250,
        null=False,
    )
    text_news = models.TextField(
        'Описание',
        null=False,
    )
    from django.utils import timezone
    preview = models.ImageField(verbose_name='Превью', null=False, upload_to='news/%Y-%m-%d/',)
    date_time = models.DateTimeField(
        verbose_name='Дата/Время публикации'
    )

    class Meta:
        verbose_name = ("Новость")
        verbose_name_plural = ("Новость")

    def __str__(self):
        return self.title


class Addimgnews(models.Model):
    idnews = models.ForeignKey(Addnews, on_delete=models.CASCADE)
    img = models.ImageField(verbose_name='Изображение', blank=True, null=True, upload_to='news/%Y-%m-%d/',)

    class Meta:
        verbose_name = ("Изображение")
        verbose_name_plural = ("Изображение")

    def __str__(self):
        return self.img.url

