import logging

import telebot
from telebot.types import KeyboardButton

from bot.constants import BotUserSteps, LanguageChoices
from bot.controllers.base import BaseController

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)


class BotController(BaseController):
    def greeting(self):
        self.sync_user()
        self.send_message(message_text=self.messages('greeting'))

    def send_exception_message_to_user(self):
        step = self.step

        if step in [BotUserSteps.LISTING_LANGUAGE, BotUserSteps.EDIT_LANGUAGE]:
            self.list_language(text=self.t('press one button'),
                               edit_lang=step == BotUserSteps.EDIT_LANGUAGE)
        elif step == BotUserSteps.MAIN_MENU:
            self.main_menu(text=self.t('press one button'))

    def back_reply_button_handler(self):
        step = self.step

        if step == BotUserSteps.EDIT_LANGUAGE:
            self.main_menu()

    def back_inline_button_handler(self):
        pass

    def list_language(self, text: str = None, edit_lang: bool = False):
        uzbek = KeyboardButton(text=self.messages('uzbek'))
        english = KeyboardButton(text=self.messages('english'))
        markup = self.reply_markup()
        markup.add(uzbek, english)
        if edit_lang:
            markup.add(self.back_reply_button)
        self.send_message(message_text=text or self.messages('select the language'), reply_markup=markup)
        self.set_step(BotUserSteps.EDIT_LANGUAGE if edit_lang else BotUserSteps.LISTING_LANGUAGE)

    def set_language(self):
        languages = {
            self.messages('english'): LanguageChoices.ENGLISH,
            self.messages('uzbek'): LanguageChoices.UZBEK
        }
        try:
            self.user.language = languages[self.message_text]
            self.user.save()
            self.main_menu(text=self.t('saved your language'))
        except KeyError:
            self.list_language(text=self.messages("selected language doesn't exist"),
                               edit_lang=self.step == BotUserSteps.EDIT_LANGUAGE)

    def main_menu(self, text: str = None, edit_message: bool = False):
        self.sync_user()
        markup = self.reply_markup()
        markup.add(KeyboardButton(text=f"{self.t('language flag')} {self.t('change language')}"))
        if edit_message:
            self.delete_message(message_id=self.callback_query_id)
        self.send_message(message_text=text or self.t('main menu'), reply_markup=markup)
        self.set_step(BotUserSteps.MAIN_MENU)
