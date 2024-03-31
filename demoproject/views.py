# used to handle errors and exceptions

from django.http import HttpResponse, HttpResponseNotFound


def handler404(request, exception):
    return HttpResponse("404: Page Not Found!<br><br><br><button>Go Back to homepage</button>")

def handler404(request, exception):
    # Adding HTML to style the 404 error page
    response = HttpResponseNotFound('<h2>Sorry, this page isn’t available.</h2>'
                                    '<p>The link you followed may be broken, or the page may have been removed.</p>'
                                    '<a href="/showform/">Go back to the homepage</a>')
    return response

