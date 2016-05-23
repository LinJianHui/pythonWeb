#coding:utf-8

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render

from learn.models import Person
# Create your views here.

def index(request):
    content = u'我是内容，来自view哦'
    mylist = Person.objects.all()
    return render(request,'home.html',{'content':content,'dics':mylist})

def add(request):
    a = request.GET.get('a',0)
    b = request.GET.get('b',0)
#     c = int(a)+int(b)
#     return HttpResponse(u'a:'+a+u'加b:'+b+u'等于c:'+str(c))
    return HttpResponseRedirect(reverse('restAdd',args=(a,b)))

def restadd(request,a,b):
    c = int(a)+int(b)
    return HttpResponse(u'a:'+a+u'加b:'+b+u'等于c:'+str(c))
def addPerson(request,username,age):
    Person.objects.create(name=username,age=age)
    return HttpResponse(u'添加'+username+u'成功')