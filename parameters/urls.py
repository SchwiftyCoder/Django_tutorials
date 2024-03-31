from django.urls import path
from . import views


# here, the endpoint also comes with extra data in angular brackets <> as part of the url itself
# this is called path parameters

urlpatterns = [
    path('getuser/<name>/<id>', views.pathview, name='pathview'), # path parameters
    path('getuser/', views.queryStringView, name='queryStringView'), # query parameters
    path('showform/', views.showform, name='showform'), # endpoint to render the form to the user
    path('getdata/', views.processFormData, name='getdata'), # endpoint to process form data
    path('dishes/<str:dish_name>', views.menuitems, name='dishes') # path parameter - single value
]

