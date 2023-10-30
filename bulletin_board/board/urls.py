from django.urls import path
from .views import AdsList, Ad, AdCreate, AdEdit, AdDelete

urlpatterns = [
    path('', AdsList.as_view(template_name='ads.html')),
    path('ads/', AdsList.as_view(), name='Ads'),
    path('ad/<int:pk>', Ad.as_view()),
    path('ad/create/', AdCreate.as_view(), name='ad_create'),
    path('ad/<int:pk>/edit/', AdEdit.as_view(), name='ad_edit'),
    path('ad/<int:pk>/delete/', AdDelete.as_view(), name='ad_delete'),
]