from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



# listens for incoming requests from the client and responds accordingly

# request: This object contains metadata about the request being made to the view, such as HTTP headers, the HTTP method (GET, POST, etc.), and any URL parameters or query parameters.

# index is a view function, first argument must always be the request object
def index(request):
    return HttpResponse("<b>Hello, world. This is the index view.</b>")
