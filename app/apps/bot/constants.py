import os

from django.db import models

BOT_TOKEN = os.environ.get('BOT_TOKEN')


class LanguageChoices(models.TextChoices):
    UZBEK = 'uz', 'Uzbek'
    ENGLISH = 'en', 'English'


class BotUserSteps(models.IntegerChoices):
    LISTING_LANGUAGE = 1, 'Listing language'
    MAIN_MENU = 2, 'Main menu'


class CallbackData:
    MAIN_MENU_BUTTON = 'MAIN_MENU_BUTTON'
    BACK_BUTTON = 'BACK_BUTTON'
    SKIP = 'SKIP'
