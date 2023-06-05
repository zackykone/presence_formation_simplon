Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from django.urls import path
... from . import views
... 
... urlpatterns = [
...     path('enregistrer/', views.enregistrer_participant, name='enregistrer_participant'),
