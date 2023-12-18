import logging
import traceback

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.constants import EXCEPTION_CHANNEL_ID, CallbackData, BotUserSteps
from bot.loader import bot
from bot.strings import messages

logger = logging.getLogger(__name__)


def send_exception(error_text, step, user=None):
    try:
        except_message = ''
        if user:
            if user.username:
                except_message = f"{messages.get('person emoji')} @{user.username}\n"
            else:
                except_message = f"{messages.get('person emoji')} <a href='tg://user?id={user.chat_id}'>{user}</a>\n"

        except_message += f"{messages.get('step emoji')} {BotUserSteps(step).label}\n\n" \
                          f"{messages.get('warning emoji')} {error_text[len(error_text) - 1020:]}"

        markup = InlineKeyboardMarkup(row_width=2)
        markup.add(InlineKeyboardButton(messages.get('condition emoji'), callback_data=CallbackData.EXCEPTION))
        bot.send_message(chat_id=EXCEPTION_CHANNEL_ID,
                         text=except_message,
                         reply_markup=markup,
                         parse_mode='HTML')
    except Exception as e:
        logger.error(traceback.format_exc())
        logger.error(e)
