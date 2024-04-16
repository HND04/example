from django.urls import path,include
from . import views,routing

urlpatterns = [
    path('a', views.index, name='index'),
    path('n', views.data_view, name='data'),
     path('', views.home, name='home'),
      path('api/', include(routing.websocket_urlpatterns)),
]


