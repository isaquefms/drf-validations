from django.urls import path

from clients.views import ClientViewSet


urlpatterns = [
    path('', ClientViewSet.as_view({'get': 'list', 'post': 'create'})),
]
