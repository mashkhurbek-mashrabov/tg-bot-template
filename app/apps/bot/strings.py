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
    },
    LanguageChoices.UZBEK: {
        'language flag': '🇺🇿',
        'main menu': '⏏️ Asosiy menu',
        'back button': '⬅️ Ortga',
        'skip': "O'tkazib yuborish ➡",
        'cancel': '❌ Bekor qilish',
        'saved your language': 'Language saved, now we will talk using this language',
    },
}
