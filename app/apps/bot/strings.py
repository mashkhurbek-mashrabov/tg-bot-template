from bot.constants import LanguageChoices

messages = {
    'greeting': '😊 Welcome!',
    'select the language': "👇 Choose a language :",
    'uzbek': "🇺🇿 O'zbek",
    'english': "🇺🇸 English",
    "selected language doesn't exist": "👇 Please choose from one of the available languages below:",

    'person emoji': '👤',
    'step emoji': '👣',
    'warning emoji': '⚠️',
    'condition emoji': '🛠',
    'next emoji': '⏭',
    'true icon': '✅',
    'false icon': '❌',
    'approved': '✅ Approved',
    'rejected': '❌ Rejected',
    'yes': "✅ Yes",
    'no': "❌ No",

    LanguageChoices.ENGLISH: {
        'language flag': '🇺🇸',
        'main menu': '⏏️ Main menu',
        'back button': '⬅️ Back',
        'skip': 'Skip ➡',
        'cancel': '❌ Cancel',
        'saved your language': 'The chosen language has been saved.',
        'exception message': "🤕 I apologize for the inconvenience, but it seems like there was a minor malfunction in the bot.",
        'press one button': "Press one of the buttons",
        'change language': 'Change language',
    },
    LanguageChoices.UZBEK: {
        'language flag': '🇺🇿',
        'main menu': '⏏️ Asosiy menu',
        'back button': '⬅️ Ortga',
        'skip': "O'tkazib yuborish ➡",
        'cancel': '❌ Bekor qilish',
        'saved your language': 'Language saved, now we will talk using this language',
        'exception message': "🤕 Kechirasiz botimizda bir oz nosozlik yuzaga keldi.",
        'press one button': "Tugmalardan birini bosing",
        'change language': "Tilni o'zgartirish",
    },
}
