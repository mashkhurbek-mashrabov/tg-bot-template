from django.core.exceptions import ValidationError
from django.db import models

from bot.constants import LanguageChoices, BotUserSteps
from common.models import BaseModel


class TelegramUser(BaseModel):
    """
    Represents a Telegram user interacting with the bot.

    Attributes:
        chat_id (models.CharField): User's unique chat_id in Telegram. (max_length=40)
        username (models.CharField): Username of the user in Telegram. (max_length=40, null=True, blank=True)
        name (models.CharField): Optional full name of the user. (max_length=40, null=True)
        language (models.CharField): User's preferred language based on `bot.constants.LanguageChoices`. (max_length=3, choices=LanguageChoices.choices, default=LanguageChoices.ENGLISH)
        step (models.SmallIntegerField): Current progress of the user within the bot flow based on `bot.constants.BotUserSteps`. (choices=BotUserSteps.choices)

    Methods:
        __str__(self): Returns a string representation of the user for debugging purposes.
    """

    chat_id = models.CharField(max_length=40, unique=True)
    username = models.CharField(max_length=40, unique=True, null=True, blank=True)
    name = models.CharField(max_length=40, null=True)
    language = models.CharField(max_length=3, choices=LanguageChoices.choices,
                                default=LanguageChoices.ENGLISH)
    step = models.SmallIntegerField(choices=BotUserSteps.choices, default=BotUserSteps.LISTING_LANGUAGE)

    def __str__(self):
        return f"{self.chat_id} - {self.name}"

    def clean(self):
        super().clean()
        if self.step not in [step[0] for step in BotUserSteps.choices]:
            raise ValueError("Invalid step value")

        if self.language not in [lang[0] for lang in LanguageChoices.choices]:
            raise ValueError("Invalid language value")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
