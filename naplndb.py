import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
import django
django.setup()

#naplň databazu

from skola.models import *
import random

Trieda.objects.all().delete() # vymaže všetky triedy
Student.objects.all().delete()
Ucitel.objects.all().delete()

# Trieda.objects.create(nazov=f"I.A") # vytvorí triedu I.A



for rocnik in range(1, 5):
    for pismeno in ['A', 'B', 'C', 'D']:
        Trieda.objects.create(nazov = f"{rocnik}.{pismeno}") # vytvorí triedu I.A
        
  
for meno in ["Ján", "Adam", "Jozef", "Tomáš"]:
    for priezvisko in ["Mrkvička", "Šarlina", "Šutek", "Trnka"]:
        titul = random.choice(["Ing.", "Mgr.", "Phdr"])
        Ucitel.objects.create(titul=titul, meno=meno, priezvisko=priezvisko)
        Student.objects.create(meno=meno, priezvisko=priezvisko, trieda=random.choice(Trieda.objects.all()))