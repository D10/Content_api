from django.db import models
from django.shortcuts import reverse


class Page(models.Model):
    title = models.CharField(verbose_name='Название', max_length=65)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    def get_absolute_url(self):
        return reverse('detail_content', kwargs={'pk': self.pk})


class Content(models.Model):
    page = models.ForeignKey(Page, verbose_name='Страница', on_delete=models.CASCADE, related_name='content')
    title = models.CharField(verbose_name='Название', max_length=65)
    counter = models.PositiveIntegerField(verbose_name='Кол-во просмотров', default=0)
    position = models.PositiveSmallIntegerField(verbose_name='Позиция', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = 'Контент'


class VideoContent(Content, models.Model):
    content = models.OneToOneField(to=Content, parent_link=True,
                                   related_name='video_content', on_delete=models.CASCADE)
    video_link = models.CharField(verbose_name='Ссылка на видео', max_length=2048)  # Такая большая макс.длина поля
    sub_link = models.CharField(verbose_name='Ссылка на субтитры', max_length=2048,  # на случай очень длиной ссылки
                                blank=True, null=True)

    class Meta:
        verbose_name = 'Видеофайл'
        verbose_name_plural = 'Видеофайлы'


class AudioContent(Content, models.Model):
    content = models.OneToOneField(to=Content, parent_link=True,
                                   related_name='audio_content', on_delete=models.CASCADE)
    bpm = models.PositiveSmallIntegerField(verbose_name='Кол-во bpm')

    class Meta:
        verbose_name = 'Аудиофайл'
        verbose_name_plural = 'Аудиофайлы'


class TextContent(Content, models.Model):
    content = models.OneToOneField(to=Content, parent_link=True,
                                   related_name='text_content', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'Текст'
        verbose_name_plural = 'Тексты'
