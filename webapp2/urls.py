
from django.urls import path
from .views import home, about, contact, contactprocess

urlpatterns = [
    path('', home),
    path('home/', home, name='homel'),
    path('about/', about, name='aboutl'),
    path('contact/', contact, name='contactl'),
    path('contactprocess/', contactprocess, name='contactprocess')
]
