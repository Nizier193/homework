from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.auth import get_user_model

User = get_user_model()

class Advertisement(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена'
    )
    auction = models.BooleanField(
        default=False,
        verbose_name='Торг'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата публикации"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата редактирования"
    )
    user = models.ForeignKey(
        User,
        verbose_name='пользователь',
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        verbose_name='изображения',
        upload_to = 'online_shop_b/',
        blank=True,
        null=True,
    )
    # from online_shop_b.models import *
    @admin.display(description='Изображение')
    def display_photo(self):
        if self.image:
            return format_html('<img src={} style="width:100px;">', self.image.url)
        else:
            return format_html('<img src="/static/img/adv.png" style="width:100px;">')

    @admin.display(description='Дата создания')
    def display_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                f'<span>Сегодня в <span style="color: blue;">{created_time}</span></span>'
            )
        return self.created_at.strftime('%d.%m.%Y в %H:%M:%S')

    @admin.display(description='Дата изменения')
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            created_time = self.updated_at.time().strftime('%H:%M:%S')
            return format_html(
                f'<span>Сегодня в <span style="color: blue;">{created_time}</span></span>'
            )
        return self.updated_at.strftime('%d.%m.%Y в %H:%M:%S')

    def __str__(self):
        return f'Advertisement(id = {self.id}, title = {self.title}, price = {self.price}, photo = {self.image})'

    class Meta:
        db_table = 'advertisements'