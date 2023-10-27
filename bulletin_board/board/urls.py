from django.urls import path
from .views import AdsList, Ad, Index

urlpatterns = [
    path('', Index.as_view(template_name='index.html')),
    path('ads/', AdsList.as_view(), name='Ads'),
    path('ad/<int:pk>', Ad.as_view()),
]