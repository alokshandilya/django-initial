from django.urls import path

from .views import about, hello, index, sum

urlpatterns = [
    path("", index),
    path("about/", about),
    path("hello/<str:user_name>/", hello),
    path("sum/<int:num1>/<int:num2>/", sum),
]
