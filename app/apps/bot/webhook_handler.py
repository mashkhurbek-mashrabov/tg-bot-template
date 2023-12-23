import logging
import traceback

import telebot
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from telebot import custom_filters, types
from telebot.util import content_type_media

from bot.constants import BotUserSteps, CallbackData
from bot.controllers.main import BotController
from bot.loader import bot
from bot.utils import send_exception

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)  # Outputs debug messages to console.


@csrf_exempt
def webhook_handler(request):
    if request.method == 'POST':
        bot.process_new_updates(
            [telebot.types.Update.de_json(
                request.body.decode("utf-8")
            )]
        )
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


@bot.message_handler(chat_id=[12345678], commands=['example'])
def admin_message_handler(message: types.Message):
    pass


@bot.message_handler(commands=['start'])
def start_handler(message: types.Message):
    controller = BotController(message, bot)
    try:
        controller.greeting()
        controller.list_language()
    except Exception as e:
        controller.main_menu(text=controller.t('exception message'))
        send_exception(traceback.format_exc(), controller.step, controller.user)


@bot.message_handler(content_types=['text'])
def message_handler(message: types.Message):
    controller = BotController(message, bot)
    user_step = controller.step
    message_text = message.text
    try:
        if message_text == controller.t('main menu'):
            controller.main_menu()
        elif message_text == controller.t('back button'):
            controller.back_reply_button_handler()
        elif message_text == f"{controller.t('language flag')} {controller.t('change language')}":
            controller.list_language(edit_lang=True)
        elif user_step in [BotUserSteps.LISTING_LANGUAGE, BotUserSteps.EDIT_LANGUAGE]:
            controller.set_language()
        else:
            controller.send_exception_message_to_user()
    except Exception as e:
        controller.main_menu(text=controller.t('exception message'))
        send_exception(traceback.format_exc(), controller.step, controller.user)


@bot.callback_query_handler(func=None)
def callback_handler(message: types.CallbackQuery):
    controller = BotController(message, bot)
    user_step = controller.step
    callback_data = message.data
    try:
        if callback_data == CallbackData.MAIN_MENU_BUTTON:
            controller.main_menu(edit_message=True)
        elif callback_data.startswith(CallbackData.BACK_BUTTON):
            controller.back_inline_button_handler()
        elif callback_data == CallbackData.EXCEPTION:
            controller.bug_fixed()
    except Exception as e:
        controller.main_menu(text=controller.t('exception message'), edit_message=True)
        send_exception(traceback.format_exc(), controller.step, controller.user)


@bot.message_handler(func=lambda message: True, content_types=content_type_media)
def general_handler(message):
    controller = BotController(message, bot)
    user_step = controller.step
    try:
        controller.send_exception_message_to_user()
    except Exception as e:
        controller.main_menu(text=controller.t('exception message'))
        send_exception(traceback.format_exc(), controller.step, controller.user)


bot.add_custom_filter(custom_filters.ChatFilter())
