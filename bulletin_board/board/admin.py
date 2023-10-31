from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

from .models import Advertisement, Response

admin.site.register(Advertisement)
admin.site.register(Response)
