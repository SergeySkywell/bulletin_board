from django.core.mail import send_mail
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from .forms import AdvertisementForm, ResponseForm
from .models import Advertisement, Response
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


def manage_responses(request):
    if not request.user.is_authenticated:
        return redirect('login')

    status_filter = request.GET.get('status')
    responses = Response.objects.filter(advertisement__author=request.user)

    if status_filter == "accepted":
        responses = responses.filter(status=True)
    elif status_filter == "pending":
        responses = responses.filter(status=False)

    ads_with_responses = Advertisement.objects.filter(id__in=responses.values_list('advertisement_id', flat=True))

    return render(request, 'manage_responses.html', {'ads_with_responses': ads_with_responses})


def accept_response(request, response_id):
    response = get_object_or_404(Response, id=response_id)
    if response.advertisement.author != request.user:
        return HttpResponseForbidden()

    response.status = True
    response.save()

    send_mail(
        'Ваш отклик был принят!',
        'Ваш отклик на объявление "{}" был принят. Спасибо за интерес!'.format(response.advertisement.title),
        'no-reply@yourdomain.com',
        [response.author.email],
        fail_silently=False,
    )

    return redirect('manage_responses')


def delete_response(request, response_id):
    response = get_object_or_404(Response, id=response_id)
    if response.advertisement.author != request.user:
        return HttpResponseForbidden()

    response.delete()
    return redirect('manage_responses')
