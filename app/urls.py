from django.urls import path
from .views import *


urlpatterns = [
    path("", home, name="home"),
    path("maisons/",maison_list ,name="maisons"),
    path("maisons/<int:numM>/details/",maison_detail ,name="detailmaisons"),
    path("maisons/<int:numM>/logements/<int:numLogement>/details/",logement_detail ,name="detaillogements"),
    path("locataires/",locataire_list ,name="locataires"),
    path("maisons/new/",new_maison ,name="new_maison"),
    path("maisons/<int:numM>/logement/new/",new_logement ,name="new_logement"),
    path("maisons/<int:numM>/depense/",maison_depense ,name="maison_depense"),
    path("maisons/logements/<int:numLogement>/depense/",logement_depense ,name="logement_depense"),
    path("maisons/logements/<int:numLogement>/<int:numLocataire>/paiement/",paiement ,name="paiement"),
    path("maisons/<int:numM>/udm",update_delete_maison,name="u_d_m"),
    path("maisons/<int:numM>/update",update_maison,name="update_maison"),
    path("maisons/<int:numM>/delete",delete_maison,name="delete_maison"),
    path("maisons/<int:numM>/logements/<int:numLogement>/udl",update_delete_logement,name="u_d_l"),
    path("maisons/<int:numM>/logements/<int:numLogement>/update",update_logement,name="update_logement"),
    path("maisons/<int:numM>/logements/<int:numLogement>/delete",delete_logement,name="delete_logement"),
    path("maisons/<int:numM>/logements/<int:numLogement>/ajoutL",add_locataire,name="add_locataire"),
    path("maisons/<int:numM>/logements/<int:numLogement>/<numLocataire>/bail",create_bail,name="bail"),
    path("bail/<int:idLocation>/usb",update_date_fin_bail,name="u_s_b"),
    path("bail/<int:idLocation>/update",updateBail,name="update_bail"),
    path("bail/<int:idLocation>/stop",stop_bail,name="stop_bail"),
]
