from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


def sobre(request):
    return HttpResponse("teste")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sobre/', sobre),
]
