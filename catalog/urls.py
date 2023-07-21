from django.urls import path
from catalog.views import index, home, contacts


urlpatterns = [
    path('', home),
    path('contacts/', contacts)
]