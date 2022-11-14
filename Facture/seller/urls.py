from django.urls import path
from seller import views

urlpatterns = [
    path('valuate/', views.InternalList.as_view()),
    path('valuate/<int:pk>/', views.InternalDetail.as_view()),
]