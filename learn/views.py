#coding:utf-8

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request,'home.html')

def add(request):
    a = request.GET.get('a',0)
    b = request.GET.get('b',0)
#     c = int(a)+int(b)
#     return HttpResponse(u'a:'+a+u'加b:'+b+u'等于c:'+str(c))
    return HttpResponseRedirect(reverse('restAdd',args=(a,b)))

def restadd(request,a,b):
    c = int(a)+int(b)
    return HttpResponse(u'a:'+a+u'加b:'+b+u'等于c:'+str(c))