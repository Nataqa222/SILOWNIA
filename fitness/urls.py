from django.urls import path
from .views import (
    TrenerDetailView, ZajeciaDetailView, ProfilUzytkownikaDetailView, KarnetDetailView,
    TrenerListView, ZajeciaListView, ProfilUzytkownikaListView, KarnetListView,
    fitness_home  # Dodanie widoku strony głównej
)

urlpatterns = [
    # Strona główna
    path("", fitness_home, name="fitness-home"),
    
    # Widoki szczegółowe (DetailView)
    path('trener/<int:pk>/', TrenerDetailView.as_view(), name='trener_detail'),
    path('zajecia/<int:pk>/', ZajeciaDetailView.as_view(), name='zajecia_detail'),
    path('profil/<int:pk>/', ProfilUzytkownikaDetailView.as_view(), name='profil_detail'),
    path('karnet/<int:pk>/', KarnetDetailView.as_view(), name='karnet_detail'),

    # Widoki list (ListView)
    path('trenerzy/', TrenerListView.as_view(), name='trener-list'),
    path('zajecia/', ZajeciaListView.as_view(), name='zajecia-list'),
    path('profile/', ProfilUzytkownikaListView.as_view(), name='profil-list'),
    path('karnety/', KarnetListView.as_view(), name='karnet-list'),
]
