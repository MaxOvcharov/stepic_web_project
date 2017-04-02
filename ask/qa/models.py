# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserManager(models.Manager):
    """Useful user db-methods"""
    def random(self):
        count = self.aggregate(ids=Count('id'))['ids']
        random_index = randint(0, count - 1)
        return self.all()[random_index]

    def next_step(self, chat_id):
        self.filter(chat_id=chat_id).update(step=F('step') + 1)


class QuestionManager(models.Manager):
    def new():
        pass

    def popular():
        pass


class Question(models.Model):
    """Information about question"""
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Полный текст вопроса")
    added_at = models.DateTimeField(blank=True, auto_now_add=True, verbose_name="Дата добавления вопроса")
    rating = models.IntegerField(default=0, verbose_name="Рейтинг вопроса")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор вопроса")
    likes = models.ManyToManyField(User, related_name='question_like_user')

    objects = QuestionManager()

    def __unicode__(self):
        return 'Title: %s; Text: %s; Added At: %s; Rating: %s; Author: %s' % \
               (self.title, self.text, self.added_at, self.rating, self.author)

    class Meta:
        db_table = 'question'
        verbose_name_plural = 'Список вопросов'


class Answer(models.Model):
    """Information about answer"""
    text = models.TextField(verbose_name="Полный текст ответа")
    added_at = models.DateTimeField(blank=True, auto_now_add=True, verbose_name="Дата добавления ответа")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор ответа")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Вопрос на который отвечают")

    def __unicode__(self):
        return 'Text: %s; Added At: %s; Author: %s; Question: %s;' % \
               (self.text, self.added_at, self.author, self.question)

    class Meta:
        db_table = 'Answer'
        verbose_name_plural = 'Список ответов'
#
# sudo /etc/init.d/mysql start
# mysql -uroot -e "CREATE USER 'admin'@'localhost'"
# mysql -uroot -e "SET PASSWORD FOR 'admin'@'localhost' = PASSWORD('pass111')"
# mysql -uroot -e "CREATE DATABASE mybase"
# mysql -uroot -e "GRANT ALL ON mybase.* TO 'admin'@'localhost'"

# mysql -uroot -e "CREATE DATABASE stepic_web;"
# mysql -uroot -e "GRANT ALL PRIVILEGES ON stepic_web.* TO 'box'@'localhost' WITH GRANT OPTION;"


