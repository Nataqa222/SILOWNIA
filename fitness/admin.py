from django.contrib import admin
from .models import ProfilUzytkownika, Trener, Zajecia, Karnet

# Powiązanie ProfilUzytkownika z User
class ProfilUzytkownikaAdmin(admin.ModelAdmin):
    model = ProfilUzytkownika
    verbose_name_plural = "Profil użytkownika"

admin.site.register(ProfilUzytkownika, ProfilUzytkownikaAdmin)

# Dodanie innych modeli do panelu admina
@admin.register(Trener)
class TrenerAdmin(admin.ModelAdmin):
    list_display = ('imie', 'nazwisko', 'specjalizacja', 'lata_w_branzy')

@admin.register(Zajecia)
class ZajeciaAdmin(admin.ModelAdmin):
    list_display = ('nazwa', 'poziom_zaawansowania', 'trener')

@admin.register(Karnet)
class KarnetAdmin(admin.ModelAdmin):
    list_display = ('uzytkownik', 'typ', 'data_rozpoczecia', 'data_wygasniecia', 'aktywny')
