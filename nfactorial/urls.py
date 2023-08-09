from django.urls import path

from . import views

urlpatterns = [
    path("", views.nfactorial, name="nfactorial"), 
    path("<int:first>/add/<int:second>/", views.add, name="add"),
    path("transform/<str:text>/", views.transform, name="transform"),
    path("check/<str:word>/", views.palindrome, name="palindrome"),
    path("calc/<int:first>/<str:operation>/<int:second>/", views.calculator, name="calculator")
]