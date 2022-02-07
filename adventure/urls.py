from webbrowser import get
from django.urls import path

from adventure import views

urlpatterns = [
    path("create-vehicle/", views.CreateVehicleAPIView.as_view()),
    path("create-service-area/", views.CreateServiceAreaAPIView.as_view()),
    path("start/", views.StartJourneyAPIView.as_view()),
    path('list-vehicle/', views.ListVehicleAPIView.as_view()),
    path('vehicle-by-plate/<str:number_plate>',
         views.GetVehicleByPlateAPIView.as_view()),
    path('list-service-area/', views.ListServiceAreaAPIView.as_view()),
    path('service-area-by-kilometer/<int:kilometer>',
         views.GetServiceAreaByKilometerAPIView.as_view()),

]
