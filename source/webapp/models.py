from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='UserInfo', verbose_name="Пользователь")
    phone = models.CharField(max_length=50, verbose_name="Телефон")
    photo = models.ImageField(verbose_name='Фотография')
    friends = models.ManyToManyField(User, blank=True, null=True, related_name="my_friends", verbose_name="Друзья")

    def __str__(self):
        return self.user.get_full_name()


class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    text = models.TextField(max_length=5000, verbose_name="Текст")
    date = models.DateTimeField(default=datetime.now, verbose_name='Дата')
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='posts_by_user', verbose_name='Автор')

    def __str__(self):
        return self.title

