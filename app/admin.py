from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Maison)
admin.site.register(Logement)
admin.site.register(Locataire)
admin.site.register(Location)
admin.site.register(Paiement)
admin.site.register(Depenser)

