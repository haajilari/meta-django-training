from django.test import TestCase
from datetime import datetime
from .models import Reservation
# Create your tests here.



class ReservationModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.reservation = Reservation.objects.create(
            name="John",
            contact="09213123",
            count=1,
            notes="nothing else matters"
        )

    def test_fields(self):
        self.assertIsInstance(self.reservation.name, str)
        self.assertIsInstance(self.reservation.contact,str)
        self.assertIsInstance(self.reservation.count, int)
        self.assertIsInstance(self.reservation.notes,str)