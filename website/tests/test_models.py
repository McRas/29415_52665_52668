from django.test import TestCase
from website.models import Record

class RecordModelTest(TestCase):
    
    def setUp(self):
        self.record = Record.objects.create(
            imie="Jan",
            nazwisko="Kowalski",
            email="jan.kowalski@example.com",
            nr_telefonu="123456789",
            adres="Ul. Przykładowa 1",
            miasto="Warszawa",
            wojewodztwo="Mazowieckie",
            kod_pocztowy="00-001"
        )

    def test_record_creation(self):
        self.assertEqual(self.record.imie, "Jan")
        self.assertEqual(self.record.nazwisko, "Kowalski")
        self.assertEqual(self.record.email, "jan.kowalski@example.com")
        self.assertEqual(self.record.nr_telefonu, "123456789")
        self.assertEqual(self.record.adres, "Ul. Przykładowa 1")
        self.assertEqual(self.record.miasto, "Warszawa")
        self.assertEqual(self.record.wojewodztwo, "Mazowieckie")
        self.assertEqual(self.record.kod_pocztowy, "00-001")
