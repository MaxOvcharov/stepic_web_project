# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class QuestionManager(models.Manager):

    def new(self):
        return self.order_by('-id')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    """Information about question"""
    title = models.CharField(max_length=150, db_index=True, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Полный текст вопроса")
    added_at = models.DateTimeField(blank=True, auto_now_add=True, verbose_name="Дата добавления вопроса")
    rating = models.IntegerField(default=0, verbose_name="Рейтинг вопроса")
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Автор вопроса")
    likes = models.ManyToManyField(User, related_name='question_like_user')

    objects = QuestionManager()

    def get_url(self):
        return reverse('question', kwargs={"id": self.id})

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'question'
        verbose_name_plural = 'Список вопросов'


class Answer(models.Model):
    """Information about answer"""
    text = models.TextField(verbose_name="Полный текст ответа")
    added_at = models.DateTimeField(blank=True, auto_now_add=True, verbose_name="Дата добавления ответа")
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Автор ответа")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Вопрос на который отвечают")

    def __unicode__(self):
        return self.text

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


