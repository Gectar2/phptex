from django.db import models

# Create your models here.


class Blockinfoaboutcollege(models.Model):
    """Основная информация на сайте"""
    title_college = models.TextField(
        'Имя организации',
        null=False,
    )
    logo_img = models.ImageField(
        blank=True,
        null=True,
        upload_to="imgesheaders",
        verbose_name="Логотип колледжа"
    )
    address = models.TextField(
        'Адресс колледжа',
        null=False
    )
    phone_one = models.CharField(
        'Номер телефона №1',
        max_length=50,
        null=False,
    )
    phone_two = models.CharField(
        'Номер телефона №2',
        max_length=50,
        blank=True, null=True,
    )
    email = models.CharField(
        'Электронная почта',
        max_length=100,
        blank=True, null=True,
    )
    link_vk = models.CharField(
        'Вконтакте',
        max_length=500,
        blank=True, null=True,
    )
    link_instagram = models.CharField(
        'Instagram',
        max_length=500,
        blank=True, null=True,
    )

    link_facebook = models.CharField(
        'Facebook',
        max_length=500,
        blank=True, null=True,
    )
    link_odnoklassniki = models.CharField(
        'Одноклассники',
        max_length=500,
        blank=True, null=True,
    )
    link_youtube = models.CharField(
        'YouTube',
        max_length=500,
        blank=True, null=True,
    )
    end_header_colg = models.CharField(
        'Конец страницы',
        max_length=100,
        blank=True, null=True,
    )
    marquee = models.TextField(
        'Бегущая строка',
        blank=True, null=True,
    )

    class Meta:
        verbose_name = ("Панель управления основной инф. (header)")
        verbose_name_plural = ("Панель управления основной инф. (header)")

    def __str__(self):
        return self.title_college


class Infodirector(models.Model):
    """Информация от директора"""
    title = models.CharField(
        'Тема',
        max_length=200,
        null=False,
    )
    dircet_img = models.ImageField(
        blank=True,
        null=True,
        upload_to="imgesdirec",
        verbose_name="Изображение директора"
    )
    offer_one = models.TextField(
        'Предложение №1',
        blank=True, null=True,
    )
    offer_two = models.TextField(
        'Предложение №2',
        blank=True, null=True,
    )
    offer_three = models.TextField(
        'Предложение №3',
        blank=True, null=True,
    )
    offer_four = models.TextField(
        'Предложение №4',
        blank=True, null=True,
    )
    sincerely_orgton = models.CharField(
        'С уважением, (наименование организации)',
        max_length=100,
        null=False,
    )
    from_name_text = models.CharField(
        'И.О. Фамилия отправителя',
        max_length=100,
        null=False,
    )

    class Meta:
        verbose_name = ("Панель управления информацией директора")
        verbose_name_plural = ("Панель управления информацией директора")

    def __str__(self):
        return self.title


class Virtualtour(models.Model):
    """Кнопка виртульного тура"""
    link_video = models.CharField(
        'Ссылка на видео',
        max_length=500,
        null=False,
    )

    class Meta:
        verbose_name = ("Редактировать кнопку 'Виртуальный тур' ")
        verbose_name_plural = ("Редактировать кнопку 'Виртуальный тур'")

    def __str__(self):
        return self.link_video


class Ourprojects(models.Model):
    """Карусель проектов"""
    img_progect = models.ImageField(
        null=False,
        upload_to="imgesprogect",
        verbose_name="Изображение для проекта(Рекомендуется 190x130)"
    )
    link_project = models.CharField(
        'Ссылка на проект',
        max_length=500,
        null=False,
    )

    class Meta:
        verbose_name = ("Панель: Наши проекты")
        verbose_name_plural = ("Панель: Наши проекты")

    def __str__(self):
        return self.link_project


class Usefullinks(models.Model):
    """Карусель полезных ссылок"""
    img_useful = models.ImageField(
        null=False,
        upload_to="imgesuseful",
        verbose_name="Изображение для полезных ссылок(Рекомендуется 190x130)"
    )
    link_useful = models.CharField(
        'Ссылка',
        max_length=500,
        null=False,
    )

    class Meta:
        verbose_name = ("Панель: Полезные ссылки")
        verbose_name_plural = ("Панель: Полезные ссылки")

    def __str__(self):
        return self.link_useful


class Ourpartners(models.Model):
    """Карусель партнёров"""
    img_partners = models.ImageField(
        null=False,
        upload_to="imgespartners",
        verbose_name="Изображение партнёра(Рекомендуется 190x130)"
    )
    link_partners = models.CharField(
        'Ссылка',
        max_length=500,
        null=False,
    )

    class Meta:
        verbose_name = ("Панель: Наши партнёры")
        verbose_name_plural = ("Панель: Наши партнёры")

    def __str__(self):
        return self.link_partners


class Fillemodels(models.Model):
    """Загрузить файлы для статистического использования"""
    title_name = models.CharField(        
        'Имя файла',
        max_length=250,
        null=False,)
    file = models.FileField(
        verbose_name='Файлы для панели', null=False, upload_to='file_panel/%Y-%m-%d/'
    )

    class Meta:
        verbose_name = ("Файлы для страниц")
        verbose_name_plural = ("Файлы для страниц")

    def __str__(self):
        return self.title_name

class SiteDopmodels(models.Model):
    """Создание сайта без привязок к панели"""
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


class Currentinfo(models.Model):
    """Карусель актуальной информации"""
    img_curinfo = models.ImageField(
        null=False,
        upload_to="imgescurrentinfo",
        verbose_name="Изображение для актуальной ифнормации(Рекомендуется 400x300)"
    )
    link_curinfo = models.CharField(
        'Ссылка',
        max_length=500,
        null=False,
    )

    class Meta:
        verbose_name = ("Панель: Актуальная информация")
        verbose_name_plural = ("Панель: Актуальная информация")

    def __str__(self):
        return self.link_curinfo
