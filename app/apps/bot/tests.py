from django.test import TestCase

from .constants import LanguageChoices, BotUserSteps
from .models import TelegramUser


class TelegramUserModelTest(TestCase):
    """
    Tests for the TelegramUser model.

    This class defines the tests for the TelegramUser model using the Django TestCase.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Creates a test TelegramUser instance for use in the tests.
        """
        TelegramUser.objects.create(
            chat_id="test_chat_id",
            username="test_username",
            name="Test User",
            language=LanguageChoices.ENGLISH,  # Assuming ENGLISH is one of the choices in LanguageChoices
            step=BotUserSteps.LISTING_LANGUAGE  # Assuming LISTING_LANGUAGE is a valid step in BotUserSteps
        )

    def test_telegram_user_creation(self):
        """
        Tests that a TelegramUser can be created with the correct attributes.
        """
        user = TelegramUser.objects.get(chat_id="test_chat_id")
        self.assertEqual(user.username, "test_username")
        self.assertEqual(user.name, "Test User")
        self.assertEqual(user.language, LanguageChoices.ENGLISH)
        self.assertEqual(user.step, BotUserSteps.LISTING_LANGUAGE)

    def test_telegram_user_string_representation(self):
        """
        Tests that the __str__ method returns the expected string representation of a TelegramUser.
        """
        user = TelegramUser.objects.get(chat_id="test_chat_id")
        expected_string = "test_chat_id - Test User"
        self.assertEqual(str(user), expected_string)

    def test_telegram_user_unique_chat_id(self):
        """
        Tests that a TelegramUser cannot be created with a duplicate chat_id.
        """
        with self.assertRaises(Exception):
            TelegramUser.objects.create(
                chat_id="test_chat_id",  # Attempting to create a user with an existing chat_id
                username="another_username",
                name="Another User",
                language=LanguageChoices.ENGLISH,
                step=BotUserSteps.MAIN_MENU
            )

    def test_telegram_user_blank_fields(self):
        """
        Tests that blank fields are handled correctly when creating a TelegramUser.
        """
        blank_user = TelegramUser.objects.create(
            chat_id='blank_chat_id',
            username=None,
            name='Test',
            language=LanguageChoices.ENGLISH,
            step=BotUserSteps.LISTING_LANGUAGE
        )
        self.assertIsNone(blank_user.username)

    def test_telegram_user_default_language(self):
        """
        Tests that the default language is set correctly when creating a TelegramUser.
        """
        default_language_user = TelegramUser.objects.create(
            chat_id='default_language_chat_id',
            username='default_language_username',
            name='Default Language User',
            step=BotUserSteps.LISTING_LANGUAGE
        )
        self.assertEqual(default_language_user.language, LanguageChoices.ENGLISH)

    def test_telegram_user_invalid_step(self):
        """
        Tests that an invalid step value raises an exception when creating a TelegramUser.
        """
        try:
            TelegramUser.objects.create(
                chat_id='invalid_step_chat_id',
                username='invalid_step_username',
                name='Invalid Step User',
                language=LanguageChoices.ENGLISH,
                step=999  # Providing an invalid step value
            )
        except ValueError:
            # Expected behavior: If ValueError is raised, the test passes
            return

        # If no ValueError is raised, the test fails
        self.fail("ValueError not raised for an invalid step")

    def test_telegram_user_update(self):
        """
        Tests that a TelegramUser can be updated with the correct attributes.
        """
        user = TelegramUser.objects.get(chat_id='test_chat_id')
        user.name = 'Updated User'
        user.save()
        updated_user = TelegramUser.objects.get(chat_id='test_chat_id')
        self.assertEqual(updated_user.name, 'Updated User')
