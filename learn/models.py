#-*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    
    createtime = models.DateTimeField(u'创建时间',auto_now_add=True,editable=True)
    updatetime = models.DateTimeField(u'更新时间',auto_now=True,null=True)
    def __unicode__(self):
        return self.name