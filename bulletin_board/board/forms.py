from django import forms
from .models import Advertisement, Response


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = [
            'title',
            'category',
            'text',
            'image',
            'upload'
        ]


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['text']
