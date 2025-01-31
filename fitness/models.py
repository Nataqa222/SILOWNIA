from django.db import models
from django.contrib.auth.models import User  # Model użytkownika Django

# Listy wyboru
POZIOM_ZAAWANSOWANIA = (
    ('poczatkujacy', 'Początkujący'),
    ('sredniozaawansowany', 'Średniozaawansowany'),
    ('zaawansowany', 'Zaawansowany'),
)

TYP_KARNETU = (
    ('miesieczny', 'Miesięczny'),
    ('trzymiesieczny', 'Trzymiesięczny'),
    ('roczny', 'Roczny'),
)

# Model Trenera
class Trener(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    lata_w_branzy = models.PositiveIntegerField()
    specjalizacja = models.TextField()

    def __str__(self):
        return f"{self.imie} {self.nazwisko} - {self.specjalizacja}"

# Model Zajęć
class Zajecia(models.Model):
    nazwa = models.CharField(max_length=100)
    poziom_zaawansowania = models.CharField(max_length=20, choices=POZIOM_ZAAWANSOWANIA)
    trener = models.ForeignKey(Trener, on_delete=models.CASCADE)
    opis = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nazwa} ({self.poziom_zaawansowania})"

# Model Profilu Użytkownika
class ProfilUzytkownika(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wiek = models.PositiveIntegerField()
    poziom_zaawansowania = models.CharField(max_length=20, choices=POZIOM_ZAAWANSOWANIA, default='poczatkujacy')
    ulubione_zajecia = models.ManyToManyField(Zajecia, blank=True)
    data_rejestracji = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.user.email}"

    class Meta:
        verbose_name = "Profil użytkownika"
        verbose_name_plural = "Profile użytkowników"

# Model Karnetu
class Karnet(models.Model):
    uzytkownik = models.ForeignKey(ProfilUzytkownika, on_delete=models.CASCADE, related_name="karnety")
    typ = models.CharField(max_length=20, choices=TYP_KARNETU)
    data_rozpoczecia = models.DateField()
    data_wygasniecia = models.DateField()
    aktywny = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.uzytkownik} - {self.typ} (do {self.data_wygasniecia})"

    class Meta:
        verbose_name = "Karnet"
        verbose_name_plural = "Karnety"

