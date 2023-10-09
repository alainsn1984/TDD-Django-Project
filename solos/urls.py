from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='home'),
    path('solos/<pk>/', views.SoloDetailView.as_view(), name='solo-detail'),
]
