from django.urls import path, reverse
from .views import home
urlpatterns = [
    path('', home),
]
