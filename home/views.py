from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is home page and you can access all kind of general data from here")

def about(request):
    return HttpResponse("this is about page and here you can search all kind of about function")

def infromation(request):
    return HttpResponse("and here you  are able to access all information related to us")

def members(request):
    return HttpResponse("this is the page which provide the detail of all members which are employed by us")
