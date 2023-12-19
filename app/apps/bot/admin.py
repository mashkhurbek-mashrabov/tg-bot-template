import json

from django.contrib import admin
from django.core.serializers import serialize
from django.http import HttpResponse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from bot.models import TelegramUser

admin.site.site_header = _('Administration')


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('chat_id', 'user_name', 'language', 'created_at',)
    list_filter = ('language', 'created_at',)
    search_fields = ('username', 'chat_id', 'name',)
    search_help_text = _('Username or chat id of the user')
    actions = ('export_to_json',)
    fieldsets = (
        (_('User Details'), {
            'fields': ('chat_id', 'username', 'name', 'language', 'step',)
        }),
        (_('Creation date'), {
            'fields': ('created_at', 'updated_at',),
            'classes': ('collapse',),
            'description': format_html('<p style="color: green">The date and time when the user was created.</p>'),
        }),
    )
    readonly_fields = ('created_at', 'updated_at',)

    def user_name(self, obj):
        if obj.username:
            return format_html("<a target='_blank' href='https://t.me/{0}'>{1}</a>", obj.username, obj.name)
        return obj.name or '-'

    user_name.short_description = _('Name')
    user_name.admin_order_field = 'name'
    user_name.allow_tags = True

    def export_to_json(self, request, queryset):
        """
            Exports a list of users to a JSON file.
        """
        data = serialize('json', queryset, fields=(
            'id',
            'chat_id',
            'username',
            'name',
            'language',
            'step',
            'created_at',
            'updated_at'))

        parsed_data = json.loads(data)
        indented_data = json.dumps(parsed_data, ensure_ascii=False, indent=4)

        response = HttpResponse(indented_data, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="telegram_users.json"'
        return response

    export_to_json.short_description = _('Export to JSON')
