from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CartApiView


urlpatterns = [
    path('cart/', CartApiView.as_view())

]