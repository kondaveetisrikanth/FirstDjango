from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import UserDetails
# Create your views here.

def html_page(request):
    return render(request, 'index.html')

def sayhello(request):
    return HttpResponse("Django Project is Created")

def members(request):
    myusers = UserDetails.objects.all().values()
    template= loader.get_template('all_users.html')
    context = {
        'myusers': myusers,
    }
    return HttpResponse(template.render(context,request))

# Detials is adding because weneeds to get details wrto addded items in details.html and firname and id
def details(request,id):
    myusers = UserDetails.objects.get(id=id)
    template= loader.get_template('details.html')
    context = {
        'myusers': myusers,
    }
    return HttpResponse(template.render(context,request))