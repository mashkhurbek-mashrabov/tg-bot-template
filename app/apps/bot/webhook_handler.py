import telebot
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from telebot import custom_filters
from telebot.util import content_type_media

from bot.constants import BotUserSteps
from bot.controllers.main import BotController
from bot.loader import bot


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


@bot.message_handler(chat_id=12345678, commands='example')
def admin_message_handler(message):
    pass


@bot.message_handler(commands=['start'])
def start_handler(message):
    controller = BotController(message, bot)
    controller.greeting()
    controller.list_language()


@bot.message_handler(content_types=['text'])
def message_handler(message):
    controller = BotController(message, bot)
    user_step = controller.step
    message_text = message.text

    if message_text == controller.t('main menu'):
        controller.main_menu()
    elif message_text == controller.t('back button'):
        controller.back_reply_button_handler()
    elif message_text == f"{controller.t('language flag')} {controller.t('change language')}":
        controller.list_language(edit_lang=True)
    elif user_step in [BotUserSteps.LISTING_LANGUAGE, BotUserSteps.EDIT_LANGUAGE]:
        controller.set_language()


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(message):
    pass


@bot.message_handler(func=lambda message: True, content_types=content_type_media)
def general_handler(message):
    pass


bot.add_custom_filter(custom_filters.ChatFilter())
