from django.shortcuts import render

from .models import Advertisement
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class AdsList(ListView):
    model = Advertisement
    template_name = 'ads.html'
    context_object_name = 'ads'
    paginate_by = 10


class Ad(DetailView):
    template_name = 'ad.html'
    context_object_name = 'ad'
    queryset = Advertisement.objects.all()
