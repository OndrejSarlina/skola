from django.contrib import admin
from .models import Student, Ucitel, Trieda # importuje modely

# Register your models here.

admin.site.register(Student) # zarejestruje model studenta 
admin.site.register(Ucitel) # zarejestruje model ucitela
admin.site.register(Trieda) # zarejestruje model triedy