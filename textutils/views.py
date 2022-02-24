#created this file 

from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    #params={'name':'kishan','place':"DBG"}
    return render(request,'index.html')
   # return HttpResponse("HomePage <br> <a href='http://www.google.com' target='blank' > Google  </a> <br> <a href='/removepunc'>  removepunc </a> <br> <a href='/capfirst'>  capfirst </a> <br> <a href='/newlineremove'>  newlineremove </a> <br> <a href='/spaceremove'>  spaceremove </a> <br> <a href='/charcount'>  charcount </a>")

def about(request):
    return HttpResponse("<h1> about page </h1>")

def file(request):
    file=open("textutils/a.txt","r")
    data=file.read()
    return HttpResponse(data)

def removepunc(request):
    webtext=(request.GET.get('text','default'))
    print(webtext)
    return HttpResponse("remove punctuation <br> <a href='/' >  Home </a>" )

def capfirst(request):
    return HttpResponse("First letter capital <br> <a href='/' >  Home </a>" )

def newlineremove(request):
    return HttpResponse("remove new line <br> <a href='/' >  Home </a>" )

def spaceremove(request):
    return HttpResponse("remove space <br> <a href='/' >  Home </a>" )

def charcount(request):
    return HttpResponse("count the character <br> <a href='/' >  Home </a>" )
