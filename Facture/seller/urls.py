from django.urls import path
from seller import views


app_name = 'seller'

urlpatterns = [
    path('api/facture', views.InternalListView.as_view(), name='api_data'),
    path('api/facture/<int:pk>', views.InternalDetailListView.as_view(), name='detail'),
    # path('api/facture/filters', views.InternalDetailFilterView.as_view(), name='filters'),
    # path('', views.InternalCreateData.as_view(), name='html_create'),
    # path('html_data/', views.InternalListData.as_view(), name='html_data'),
    # path('<int:pk>/', views.InternalDetailView.as_view(), name='html_detail'),
    # path('<int:pk>/update/', views.InternalDetailUpdate.as_view(), name='html_update'),
    # path('<int:pk>/delete/', views.InternalDetailDelete.as_view(), name='html_delete'),
]
