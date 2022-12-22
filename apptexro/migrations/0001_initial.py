# Generated by Django 4.1.2 on 2022-12-20 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blockinfoaboutcollege',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_college', models.TextField(verbose_name='Имя организации')),
                ('logo_img', models.ImageField(blank=True, null=True, upload_to='imgesheaders', verbose_name='Логотип колледжа')),
                ('address', models.TextField(verbose_name='Адресс колледжа')),
                ('phone_one', models.CharField(max_length=50, verbose_name='Номер телефона №1')),
                ('phone_two', models.CharField(blank=True, max_length=50, null=True, verbose_name='Номер телефона №2')),
                ('email', models.CharField(blank=True, max_length=100, null=True, verbose_name='Электронная почта')),
                ('link_vk', models.CharField(blank=True, max_length=500, null=True, verbose_name='Вконтакте')),
                ('link_instagram', models.CharField(blank=True, max_length=500, null=True, verbose_name='Instagram')),
                ('link_facebook', models.CharField(blank=True, max_length=500, null=True, verbose_name='Facebook')),
                ('link_odnoklassniki', models.CharField(blank=True, max_length=500, null=True, verbose_name='Одноклассники')),
                ('link_youtube', models.CharField(blank=True, max_length=500, null=True, verbose_name='YouTube')),
                ('end_header_colg', models.CharField(blank=True, max_length=100, null=True, verbose_name='Конец страницы')),
                ('marquee', models.TextField(blank=True, null=True, verbose_name='Бегущая строка')),
            ],
            options={
                'verbose_name': 'Панель управления основной инф. (header)',
                'verbose_name_plural': 'Панель управления основной инф. (header)',
            },
        ),
        migrations.CreateModel(
            name='Currentinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_curinfo', models.ImageField(upload_to='imgescurrentinfo', verbose_name='Изображение для актуальной ифнормации(Рекомендуется 400x300)')),
                ('link_curinfo', models.CharField(max_length=500, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Панель: Актуальная информация',
                'verbose_name_plural': 'Панель: Актуальная информация',
            },
        ),
        migrations.CreateModel(
            name='Fillemodels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_name', models.CharField(max_length=250, verbose_name='Имя файла')),
                ('file', models.FileField(upload_to='file_panel/%Y-%m-%d/', verbose_name='Файлы для панели')),
            ],
            options={
                'verbose_name': 'Файлы для страниц',
                'verbose_name_plural': 'Файлы для страниц',
            },
        ),
        migrations.CreateModel(
            name='Infodirector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Тема')),
                ('dircet_img', models.ImageField(blank=True, null=True, upload_to='imgesdirec', verbose_name='Изображение директора')),
                ('offer_one', models.TextField(blank=True, null=True, verbose_name='Предложение №1')),
                ('offer_two', models.TextField(blank=True, null=True, verbose_name='Предложение №2')),
                ('offer_three', models.TextField(blank=True, null=True, verbose_name='Предложение №3')),
                ('offer_four', models.TextField(blank=True, null=True, verbose_name='Предложение №4')),
                ('sincerely_orgton', models.CharField(max_length=100, verbose_name='С уважением, (наименование организации)')),
                ('from_name_text', models.CharField(max_length=100, verbose_name='И.О. Фамилия отправителя')),
            ],
            options={
                'verbose_name': 'Панель управления информацией директора',
                'verbose_name_plural': 'Панель управления информацией директора',
            },
        ),
        migrations.CreateModel(
            name='Ourpartners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_partners', models.ImageField(upload_to='imgespartners', verbose_name='Изображение партнёра(Рекомендуется 190x130)')),
                ('link_partners', models.CharField(max_length=500, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Панель: Наши партнёры',
                'verbose_name_plural': 'Панель: Наши партнёры',
            },
        ),
        migrations.CreateModel(
            name='Ourprojects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_progect', models.ImageField(upload_to='imgesprogect', verbose_name='Изображение для проекта(Рекомендуется 190x130)')),
                ('link_project', models.CharField(max_length=500, verbose_name='Ссылка на проект')),
            ],
            options={
                'verbose_name': 'Панель: Наши проекты',
                'verbose_name_plural': 'Панель: Наши проекты',
            },
        ),
        migrations.CreateModel(
            name='SiteDopmodels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_link', models.CharField(max_length=250, verbose_name='Имя ссылки')),
                ('name_page', models.CharField(max_length=250, verbose_name='Имя страницы')),
                ('content_text', models.TextField(verbose_name='Информационный блок')),
            ],
            options={
                'verbose_name': 'Добавить страницу',
                'verbose_name_plural': 'Добавить страницу',
            },
        ),
        migrations.CreateModel(
            name='Usefullinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_useful', models.ImageField(upload_to='imgesuseful', verbose_name='Изображение для полезных ссылок(Рекомендуется 190x130)')),
                ('link_useful', models.CharField(max_length=500, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Панель: Полезные ссылки',
                'verbose_name_plural': 'Панель: Полезные ссылки',
            },
        ),
        migrations.CreateModel(
            name='Virtualtour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_video', models.CharField(max_length=500, verbose_name='Ссылка на видео')),
            ],
            options={
                'verbose_name': "Редактировать кнопку 'Виртуальный тур' ",
                'verbose_name_plural': "Редактировать кнопку 'Виртуальный тур'",
            },
        ),
    ]