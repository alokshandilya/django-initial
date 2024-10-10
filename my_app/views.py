from django.shortcuts import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")


def about(request):
    return HttpResponse("About page")


def hello(request, user_name):
    return HttpResponse(f"Hello, {user_name}")


def sum(request, num1, num2):
    return HttpResponse(f"sum: {num1 + num2}")
