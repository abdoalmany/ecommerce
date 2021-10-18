from django.urls import path
from . import views
urlpatterns = [
    path('', views.store , name = "store"),
    path('', views.cart , name = "cart"),
    path('', views.checkout , name = "checkout"),
]
