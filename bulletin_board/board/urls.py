from django.urls import path
from .views import AdsList, Ad

urlpatterns = [
    path('', AdsList.as_view(template_name='ads.html')),
    path('ads/', AdsList.as_view(), name='Ads'),
    path('ad/<int:pk>', Ad.as_view()),
]