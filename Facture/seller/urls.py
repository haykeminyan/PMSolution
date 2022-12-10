from django.urls import path
from seller import views


app_name = "seller"

urlpatterns = [
    path('', views.InternalCreateData.as_view(), name='create'),
    path('all_data', views.InternalAllData.as_view(), name='all_data'),
    path('<pk>/', views.InternalDetailView.as_view(), name='detail'),
    path('<pk>/update/', views.InternalDetailUpdate.as_view(), name='update'),
    path('<pk>/delete/', views.InternalDetailDelete.as_view(), name='delete'),
]