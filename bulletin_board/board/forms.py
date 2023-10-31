from django import forms
from .models import Advertisement, Response


# Форма для объявления
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


# Форма для отклика
class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['text']


# Форма для новостной рассылки
class NewsletterForm(forms.Form):
    subject = forms.CharField(max_length=200, label="Тема")
    message = forms.CharField(widget=forms.Textarea, label="Сообщение")
