from django.urls import path
from seller import views


app_name = "seller"

urlpatterns = [
    path('valuate/', views.InternalList.as_view()),
    path('valuate/<int:pk>/', views.InternalDetail.as_view()),
    path('', views.index, name='index'),
    path('valuate', views.valuate, name='valuate')
]