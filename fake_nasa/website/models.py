from django.db import models
from filer.models import File


class CustomFile(File):
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name='Сортировка'
    )

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'
        ordering = ('my_order',)
