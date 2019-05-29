# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
    first_name=models.CharField(max_length=250,blank=False,default='')
    last_name=models.CharField(max_length=250,blank=False,default='')
    age=models.CharField(max_length=3)
    @classmethod
    def create_person(self,first_name,last_name,age):
        person=self(first_name,last_name,age)
        return person.id
    class Meta:
        ordering=('id',)
