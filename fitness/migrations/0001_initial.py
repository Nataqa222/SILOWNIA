import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trener',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=50)),
                ('nazwisko', models.CharField(max_length=50)),
                ('lata_w_branzy', models.PositiveIntegerField()),
                ('specjalizacja', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProfilUzytkownika',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wiek', models.PositiveIntegerField()),
                ('poziom_zaawansowania', models.CharField(choices=[('poczatkujacy', 'Początkujący'), ('sredniozaawansowany', 'Średniozaawansowany'), ('zaawansowany', 'Zaawansowany')], default='poczatkujacy', max_length=20)),
                ('data_rejestracji', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profil użytkownika',
                'verbose_name_plural': 'Profile użytkowników',
            },
        ),
        migrations.CreateModel(
            name='Karnet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typ', models.CharField(choices=[('miesieczny', 'Miesięczny'), ('trzymiesieczny', 'Trzymiesięczny'), ('roczny', 'Roczny')], max_length=20)),
                ('data_rozpoczecia', models.DateField()),
                ('data_wygasniecia', models.DateField()),
                ('aktywny', models.BooleanField(default=True)),
                ('uzytkownik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='karnety', to='fitness.profiluzytkownika')),
            ],
            options={
                'verbose_name': 'Karnet',
                'verbose_name_plural': 'Karnety',
            },
        ),
        migrations.CreateModel(
            name='Zajecia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
                ('poziom_zaawansowania', models.CharField(choices=[('poczatkujacy', 'Początkujący'), ('sredniozaawansowany', 'Średniozaawansowany'), ('zaawansowany', 'Zaawansowany')], max_length=20)),
                ('opis', models.TextField(blank=True, null=True)),
                ('trener', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitness.trener')),
            ],
        ),
        migrations.AddField(
            model_name='profiluzytkownika',
            name='ulubione_zajecia',
            field=models.ManyToManyField(blank=True, to='fitness.zajecia'),
        ),
    ]
