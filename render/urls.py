from django.urls import path

from . import views

urlpatterns = [
    path('a', views.index, name='index'),
    path('', views.data_view, name='data'),
]



