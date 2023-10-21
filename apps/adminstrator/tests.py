from django.test import TestCase
from .models import Announcement

class TestAnnouncement(TestCase):
    def setUp(self) -> None:
        self.announcement = Announcement(
            headline='Test Headline',
            description='Test description'
        )
        def test_announcement_model(self):
            self.assertEqual(self.announcement.headline, 'Test Headline')
            self.assertEqual(self.announcement.description, 'Test description')
