from django.urls import path
from . import views
from .views import AdsList, Ad, AdCreate, AdEdit, AdDelete, create_response

urlpatterns = [
    path('', AdsList.as_view(template_name='ads.html')),
    path('ads/', AdsList.as_view(), name='Ads'),
    path('ad/<int:pk>', Ad.as_view(), name='ad_detail'),
    path('ad/create/', AdCreate.as_view(), name='ad_create'),
    path('ad/<int:pk>/edit/', AdEdit.as_view(), name='ad_edit'),
    path('ad/<int:pk>/delete/', AdDelete.as_view(), name='ad_delete'),
    path('ad/<int:pk>/response/', views.create_response, name='create_response'),
    path('my-responses/', views.manage_responses, name='manage_responses'),
    path('accept-response/<int:response_id>/', views.accept_response, name='accept_response'),
    path('delete-response/<int:response_id>/', views.delete_response, name='delete_response'),
]