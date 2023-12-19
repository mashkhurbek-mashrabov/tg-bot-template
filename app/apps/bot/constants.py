import os

from django.db import models

BOT_TOKEN = os.environ.get('BOT_TOKEN')
EXCEPTION_CHANNEL_ID = os.environ.get('EXCEPTION_CHANNEL_ID')
WEBHOOK_URL_PATH = 'bot/'


class LanguageChoices(models.TextChoices):
    UZBEK = 'uz', 'Uzbek'
    ENGLISH = 'en', 'English'


class BotUserSteps(models.IntegerChoices):
    LISTING_LANGUAGE = 1, 'Listing language'
    EDIT_LANGUAGE = 2, 'Edit language'
    MAIN_MENU = 3, 'Main menu'


class CallbackData:
    MAIN_MENU_BUTTON = 'MAIN_MENU_BUTTON'
    BACK_BUTTON = 'BACK_BUTTON'
    SKIP = 'SKIP'
    EXCEPTION = 'EXCEPTION'
