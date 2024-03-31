from django.shortcuts import render
from django.http import HttpResponse


# this view serves path parameters
# exampple URL: http://example.com/customer/5
# URL dispatcher should identify John as the name parameter and 1 as the id parameter. 
# these must eb parsed directly to the corresponding view function for processing
def pathview(request, name, id):
    return HttpResponse(f"Name: {name}<br>UserID: {id}")


# this view serves query parameters
# these type of parameters are not parsed by the url dispatcher
# rather, they are part of the request.get property as a key-value pair
# example URL: http://localhost:8000/getuser/?name=John&id=1
# we do not need to check if the request method is a GET because it is the default when none is specified
def queryStringView(request):
    name = request.GET["name"]
    id = request.GET["id"]
    return HttpResponse(f"name: {name}<br>id: {id}")


# another view function that renders an html page when called by the url pattern dispatcher
def showform(request):
    return render(request, "parameters/form.html")


# a view function that processes forms
def processFormData(request):
    if request.method == "POST":
        name = request.POST["name"]
        id = request.POST["id"]

    return HttpResponse(f"name: {name}<br>id: {id}")


# path converters
# the URL dispathcer must identify the value and type and pass the value to the view function
def menuitems(request, dish_name):
    items = {
        "s": "A classic Italian pasta dish made with egg, hard cheese, cured pork, and black pepper.",
        "Ratatouille": "A French Provencal stewed vegetable dish, originating in Nice, featuring eggplant, zucchini, bell peppers, and tomatoes.",
        "sushi": "A traditional Japanese dish of prepared vinegared rice, usually with some sugar and salt, accompanying a variety of ingredients such as seafood, often raw, and vegetables.",
        "tacos": "A dish developed in Central Mexico, based on shawarma spit-grilled meat, brought by Lebanese immigrants to Mexico, featuring pork marinated in a blend of dried chilies, spices, and pineapple.",
        "massaman": "A rich, relatively mild Thai curry that includes dried spices like cinnamon, star anise, and cardamom, typically made with beef, but also can be made with chicken, duck, or tofu.",
    }

    item_name = dish_name.strip()
    item_desc = items.get(dish_name.strip(), "Dish Description not Found!")

    return HttpResponse(f"<h1>{item_name}</h1><br><br>{item_desc}")
