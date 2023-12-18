from django.db import models


class LanguageChoices(models.TextChoices):
    UZBEK = 'uz', 'Uzbek'
    ENGLISH = 'en', 'English'


class BotUserSteps(models.IntegerChoices):
    LISTING_LANGUAGE = 1, 'Listing language'
    MAIN_MENU = 2, 'Main menu'
