from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import AdvertisementForm
from .models import Advertisement
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin


class AdsList(ListView):
    model = Advertisement
    template_name = 'ads.html'
    context_object_name = 'ads'
    paginate_by = 10


class Ad(DetailView):
    template_name = 'ad.html'
    context_object_name = 'ad'
    queryset = Advertisement.objects.all()


class AdCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('board.add_advertisement',)
    form_class = AdvertisementForm
    model = Advertisement
    template_name = 'ad_edit.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class AdEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('board.change_advertisement',)
    form_class = AdvertisementForm
    model = Advertisement
    template_name = 'ad_edit.html'


class AdDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('board.delete_advertisement',)
    model = Advertisement
    template_name = 'ad_delete.html'
    success_url = reverse_lazy('ads')
