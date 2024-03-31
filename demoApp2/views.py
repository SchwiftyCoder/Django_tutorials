from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    path = request.path 
    request_obj = f"path: {request.path}<br>scheme: {request.scheme}<br>method: {request.method}<br>\
        Address: {request.META['REMOTE_ADDR']}<br>user_agent: {request.META['HTTP_USER_AGENT']}<br>path info: {request.path_info}"
    return HttpResponse(request_obj)