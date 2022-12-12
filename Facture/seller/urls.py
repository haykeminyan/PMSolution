from django.urls import path
from seller import views


app_name = 'seller'

urlpatterns = [
    path('', views.InternalCreateData.as_view(), name='create'),
    path('list_data/', views.InternalListData.as_view(), name='list_data'),
    path('<int:pk>/', views.InternalDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', views.InternalDetailUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.InternalDetailDelete.as_view(), name='delete'),
]
