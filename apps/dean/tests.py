from django.test import TestCase
from apps.dean.models import Dean, Deputy

class TestDean(TestCase):
    def setUp(self) -> None:
        self.d = Dean.objects.create(
            email='dean@c.com',
            first_name='John',
            d_o_b='1999-1-2',
            last_name='Smith',
            gender='Male',
        )
        self.dp = Deputy.objects.create(
            email='test@c.com',
            first_name='John',
            last_name='Sue',
            d_o_b='1999-1-2',
            gender='Male',
        )

    def test_str_return(self):
        self.assertEqual(str(self.d), 'Sir Smith')
