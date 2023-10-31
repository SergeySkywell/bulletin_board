from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from .forms import AdvertisementForm, ResponseForm
from .models import Advertisement
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin


class AdsList(ListView):
    model = Advertisement
    template_name = 'ads.html'
    context_object_name = 'Ads'
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
    success_url = reverse_lazy('Ads')


def create_response(request, pk):
    ad = get_object_or_404(Advertisement, id=pk)
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.advertisement = ad
            response.author = request.user
            response.save()

            # Отправка уведомления автору объявления
            send_mail(
                'Новый отклик на ваше объявление',
                f'{request.user} ответил на ваше объявление "{ad.title}".',
                'no-reply@yourwebsite.com',
                [ad.author.email],
                fail_silently=False,
            )

            return redirect('ad_detail', pk=pk)
    else:
        form = ResponseForm()
    return render(request, 'response_form.html', {'form': form, 'ad': ad})
