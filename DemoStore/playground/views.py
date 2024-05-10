from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#request--> RESPONSE
def say_hello(request):
    #pull data from Db
    # return render(request, 'hello.html', {'name': 'World'})
    # return HttpResponse('Hello, World!')
    return render(request, './hello.html',{'name':'Jatin'})
