import requests
from django.core.management import BaseCommand

from bot.constants import BOT_TOKEN, WEBHOOK_URL_PATH
from common.constants import DOMAIN


class Command(BaseCommand):
    help = 'Run webhook'

    def handle(self, *args, **options):
        requests.get(f'https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?url={DOMAIN}/{WEBHOOK_URL_PATH}')
        print(f'https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?url={DOMAIN}/{WEBHOOK_URL_PATH}')
        self.stdout.write(self.style.SUCCESS('Webhook is running'))