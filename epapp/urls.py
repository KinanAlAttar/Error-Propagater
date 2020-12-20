from django.urls import path
from . import views

urlpatterns = [
    # ex: /epapp/
    path('epapp/', views.index, name='index'),
    path('epapp/results', views.submit, name='submit'),
]
