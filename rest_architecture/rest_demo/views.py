# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Person
from django.shortcuts import render
from django.http import JsonResponse;
from django.http import HttpResponse
from django.template import RequestContext
# Create your views here.
def index(request):
    #context = RequestContext(request)
    persons_list=Person.objects.all()
    counter=1
    persons={}
    for person in Person.objects.all():
        persons[str(counter)]=person
        counter+=1
    persons_dict={"persons":persons}
    return render(request, 'index.html', persons_dict)
    #return render_to_response('index.html',persons_dict,context)
def delete_person(request):
    id=request.GET.get('pk',None)
    Person.objects.filter(id=id).delete()
    return HttpResponse(200);
def add_person(request):
    first_name=request.GET.get('firstName',None)
    last_name=request.GET.get('lastName',None)
    age=int(request.GET.get('age',None))
    pk=Person.create_person(first_name,last_name,age)
    return HttpResponse(str(pk),200);
    
