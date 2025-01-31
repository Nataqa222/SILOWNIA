from django.views.generic import DetailView, ListView  # Importujemy DetailView i ListView
from .models import Trener, Zajecia, ProfilUzytkownika, Karnet  # Import modeli

# Widoki szczegółowe (DetailView)
class TrenerDetailView(DetailView):
    model = Trener
    template_name = 'fitness/trener_detail.html'
    context_object_name = 'trener'

class ZajeciaDetailView(DetailView):
    model = Zajecia
    template_name = 'fitness/zajecia_detail.html'
    context_object_name = 'zajecia'

class ProfilUzytkownikaDetailView(DetailView):
    model = ProfilUzytkownika
    template_name = 'fitness/profil_uzytkownika_detail.html'
    context_object_name = 'profil'

class KarnetDetailView(DetailView):
    model = Karnet
    template_name = 'fitness/karnet_detail.html'
    context_object_name = 'karnet'

# Widoki listy (ListView)
class TrenerListView(ListView):
    model = Trener
    template_name = 'fitness/trener_list.html'
    context_object_name = 'trenerzy'

class ZajeciaListView(ListView):
    model = Zajecia
    template_name = 'fitness/zajecia_list.html'
    context_object_name = 'zajecia'

class ProfilUzytkownikaListView(ListView):
    model = ProfilUzytkownika
    template_name = 'fitness/profil_list.html'
    context_object_name = 'profile'

class KarnetListView(ListView):
    model = Karnet
    template_name = 'fitness/karnet_list.html'
    context_object_name = 'karnety'
    
from django.shortcuts import render

def fitness_home(request):
    return render(request, "fitness/home.html")
