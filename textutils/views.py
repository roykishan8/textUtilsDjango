#created this file 

import re
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    #params={'name':'kishan','place':"DBG"}
    return render(request,'index.html')
   # return HttpResponse("HomePage <br> <a href='http://www.google.com' target='blank' > Google  </a> <br> <a href='/removepunc'>  removepunc </a> <br> <a href='/capfirst'>  capfirst </a> <br> <a href='/newlineremove'>  newlineremove </a> <br> <a href='/spaceremove'>  spaceremove </a> <br> <a href='/charcount'>  charcount </a>")

def analyze(request):
    webtext=(request.GET.get('text','default'))
    removepunc=(request.GET.get('removepunc','off'))
    capital=(request.GET.get('capital','off'))
    newlineremove=(request.GET.get('newlineremove','off'))
    removespace=(request.GET.get('removespace','off'))
    charcount=(request.GET.get('charcount','off'))
    if removepunc=="on":
        analyzedtext=""
        punctuations= '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in webtext:
            if char not in punctuations:
                analyzedtext+=char
        params={'purpose':'Removed Punctuation','analyzed':analyzedtext}
        return render(request,'analyze.html',params)
    elif capital=="on":
        analyzedtext=""
        for char in webtext:
            analyzedtext+=char.upper()
        params={'purpose':'CAPTIALIZED TEXT','analyzed':analyzedtext}
        return render(request,'analyze.html',params)
    elif newlineremove=="on":
        analyzedtext=""
        for char in webtext:
            if char!='\n':
                analyzedtext+=char
        params={'purpose':'New Line Removed','analyzed':analyzedtext}
        return render(request,'analyze.html',params)
    elif removespace=="on":
        analyzedtext=""
        for index,char in enumerate(webtext):
            if not (webtext[index]==" "and webtext[index+1]==" "):
                analyzedtext+=char
        params={'purpose':'Extra Space Removed','analyzed':analyzedtext}
        return render(request,'analyze.html',params)
    elif charcount=="on":
        count=0
        for char in webtext:
            count+=1
        analyzedtext="Total character count : "+str(count)
        params={'purpose':'Total character count','analyzed':analyzedtext}
        return render(request,'analyze.html',params)
        
    else:
        return HttpResponse("error 404!!!!!!!")
     
def about(request):
    return HttpResponse("<h1> about page </h1>")

def file(request):
    file=open("textutils/a.txt","r")
    data=file.read()
    return HttpResponse(data)

# def removepunc(request):
#     webtext=(request.GET.get('text','default'))
#     print(webtext)
#     return HttpResponse("remove punctuation <br> <a href='/' >  Home </a>" )

# def capfirst(request):
#     return HttpResponse("First letter capital <br> <a href='/' >  Home </a>" )

# def newlineremove(request):
#     return HttpResponse("remove new line <br> <a href='/' >  Home </a>" )

# def spaceremove(request):
#     return HttpResponse("remove space <br> <a href='/' >  Home </a>" )

# def charcount(request):
#     return HttpResponse("count the character <br> <a href='/' >  Home </a>" )
