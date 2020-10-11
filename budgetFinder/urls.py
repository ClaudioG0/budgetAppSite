from django.urls import include, path
from . import views

urlpatterns = [
    path("main/", views.index, name="mainPage"),
    path("main/overspending/", views.overSpending, name="overSpending"),
    path('main/shopping/', views.shopping, name="shopping"),
]