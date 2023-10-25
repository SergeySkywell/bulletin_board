from django.db import models
from django.contrib.auth.models import User


class Advertisement(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    TANKS = 'TN'
    HEALERS = 'HL'
    DAMAGEDEALERS = 'DD'
    MERCHANTS = 'MC'
    GUILDMASTERS = 'GM'
    QUESTGIVERS = 'QG'
    BLACKSMITHS = 'BS'
    LEATHERWORKERS = 'LW'
    POTIONMASTERS = 'PM'
    SPELLMASTERS = 'SM'
    CATEGORY_CHOISES = (
        (TANKS, 'Танки'),
        (HEALERS, 'Хилы'),
        (DAMAGEDEALERS, 'ДД'),
        (MERCHANTS, 'Торговцы'),
        (GUILDMASTERS, 'Гилдмастеры'),
        (QUESTGIVERS, 'Квестгиверы'),
        (BLACKSMITHS, 'Кузнецы'),
        (LEATHERWORKERS, 'Кожевники'),
        (POTIONMASTERS, 'Зельевары'),
        (SPELLMASTERS, 'Мастера заклинаний')
    )
    category = models.CharField(max_length=2, choices=CATEGORY_CHOISES)
    dateCreation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'


class Response(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    text = models.TextField()