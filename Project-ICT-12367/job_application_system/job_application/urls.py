from django.urls import path
from .views import home, add_application, edit_application, delete_application, search_application

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_application, name='add_application'),
    path('edit/<int:pk>/', edit_application, name='edit_application'),
    path('delete/<int:pk>/', delete_application, name='delete_application'),
    path('search/', search_application, name='search_application'),
]
