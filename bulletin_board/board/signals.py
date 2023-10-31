from allauth.account.signals import user_signed_up
from django.core.mail import send_mail
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from .models import Response


@receiver(user_signed_up)
def user_signed_up_(request, user, **kwargs):
    group = Group.objects.get(name='Common')
    user.groups.add(group)