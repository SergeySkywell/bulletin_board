from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.contrib.auth.models import Group


@receiver(user_signed_up)
def user_signed_up_(request, user, **kwargs):
    group = Group.objects.get(name='Common')
    user.groups.add(group)
