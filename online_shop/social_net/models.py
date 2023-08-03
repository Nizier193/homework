from django.db import models

class Announcement(models.Model):
    person = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок',
        default='Новая запись!'
    )
    message = models.TextField(
        verbose_name='Сообщение'
    )
    picture = models.JSONField(
        verbose_name='URL-картинки',
        default={},
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата редактирования'
    )



class Person(models.Model):
    username = models.CharField(
        max_length=255,
        verbose_name='Служебное имя'
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Имя профиля'
    )
    age = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=10,
        verbose_name='Возраст',
    )
    about = models.TextField(
        default='Пользователь не добавил описание',
        verbose_name='Описание',
    )
    image = models.JSONField(
        verbose_name='Фотографии',
        default={
            'https://www.pngkey.com/png/detail/230-2301779_best-classified-apps-default-user-profile.png',
        }
    )
    friends = models.JSONField(
        verbose_name='Список друзей',
        default={
            'Nizier193',
        }
    )


