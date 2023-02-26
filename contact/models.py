from turtle import title
from django.db import models

# Create your models here.

class Contact(models.Model):
    title                                   = models.CharField(max_length=200, verbose_name='제목')
    content                                 = models.TextField(verbose_name='내용')
    created_at                              = models.DateTimeField(auto_now_add=True, verbose_name='작성일')
    updated_at                              = models.DateTimeField(auto_now=True, verbose_name='최종 수정일')
    answer                                  = models.TextField(verbose_name='답변')
    answer_at                               = models.DateTimeField(verbose_name='답변일')

    def __str__(self):
        return self.title