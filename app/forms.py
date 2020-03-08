from django import forms
from django.forms import ModelForm, TextInput, EmailInput

from .models import *



class MaisonForm(ModelForm):
    nomM = forms.CharField(max_length = 150, 
                label="Nom de la maison (optionnel)",
                widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                }
        ))
    numRueM = forms.IntegerField(
                label="Numéro de rue",
                widget=forms.TextInput(
                attrs={
                    "class": "form-control"
                }
        ))
    adresseM = forms.CharField(max_length = 150,
                label="Adresse",
                widget=forms.TextInput(
                attrs={
                    "class": "form-control"
                }
        ))
    codePostalM = forms.CharField(max_length = 5,
                label="Code postal",
                widget=forms.TextInput(
                attrs={
                    "class": "form-control"
                }
        ))
    villeM = forms.CharField(max_length = 150,
                label="Ville",
                widget=forms.TextInput(
                attrs={
                    "class": "form-control"
                }
        ))
    class Meta:
        model = Maison
        fields = ['nomM','numRueM','adresseM','codePostalM','villeM','photoM1','photoM2','photoM3']
        
        
class LogementForm(ModelForm):
    TYPE_CHOICES = (
            ('T1 avec cuisine non séparée','Studio'),
            ('1 pièce principale (à la fois chambre et salon) + 1 cuisine + 1 salle de bains (avec WC séparés ou inclus)', 'T1'),
            ('2 pièces (1 chambre + 1 salon) + 1 cuisine + 1 salle de bains (avec WC séparés ou inclus)', 'T2'),
            ( '2 pièces (1 chambre + 1 salon) dont l’une est suffisamment grande pour être séparée en deux zones distinctes + 1 cuisine + 1 salle de bains (avec WC séparés ou inclus)','T2 Bis'),
            ('3 pièces (2 chambres + 1 salon) + 1 cuisine + 1 salle de bains (avec WC séparés ou inclus)','T3'),
            (' 3 pièces (2 chambres + 1 salon) dont l’une est suffisamment grande pour être séparée en deux zones distinctes + 1 cuisine + 1 salle de bains (avec WC séparés ou inclus)','T3 Bis'),
            ('4 pièces (3 chambres + 1 salon/séjour OU 2 chambres + 1 salon + 1 salle à manger) + 1 cuisine + 1 salle de bains (avec WC séparés ou inclus)','T4'),
            (' T4 transformé en T3 en réunissant deux pièces pour en faire 1 grande','T3 T4'),
            (' 5 pièces (4 chambres + 1 salon/séjour OU 3 chambres + 1 salon + 1 salle à manger) + 1 cuisine + 1 salle de bains ou + (avec WC séparés ou inclus)','T5'),
    )
    typeL = forms.ChoiceField(label="Type",choices=TYPE_CHOICES)
    superficie = forms.IntegerField(label="Superficie",
                widget=forms.TextInput(
                attrs={
                    "class": "form-control"
                }
        ))
    loyer = forms.IntegerField(label="Loyer",
                widget=forms.TextInput(
                attrs={
                    "class": "form-control"
                }
        ))
    
    class Meta:
        model = Logement
        fields= ['typeL','superficie','loyer','photoL1','photoL2','photoL3']
    

class LocataireForm(ModelForm):
    nomLocataire = forms.CharField(max_length = 150,
                label="Nom",
                widget=forms.TextInput(
                attrs={
                    "class": "form-control"
                }
        ))
    prenomLocataire = forms.CharField(
                label="Prenom",
                widget=forms.TextInput(
                attrs={
                    "class": "form-control"
                }
        ))
    
    telephoneLocataire = forms.IntegerField(
                label="Telephone",
                widget=forms.TextInput(
                attrs={
                    "class": "form-control"
                }
        ))
    
    mailLocataire = forms.EmailField(max_length = 150,
                label="Email",
                widget=forms.EmailInput(
                attrs={
                    "class": "form-control"
                }
        ))
    profession = forms.CharField(max_length = 150,
                label="Profession",
                widget=forms.TextInput(
                attrs={
                    "class": "form-control"
                }
        ))
    
    
    class Meta:
        model = Locataire
        fields = ['nomLocataire','prenomLocataire','telephoneLocataire','mailLocataire','profession']
        

class PaiementForm(ModelForm):
    montantP = forms.IntegerField(
                label="Montant à encaisser",
                widget=forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ))
    class Meta:
        model = Paiement
        fields = ['montantP']
        
class DepenserForm(ModelForm):
    montantD = forms.IntegerField(
                label="Montant",
                widget=forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ))
    descriptionD = forms.CharField(label="Description",
                                   widget=forms.Textarea(
                                       attrs= {
                                           "class": "form-control"
                                       }
                                   ))
    class Meta:
        model = Paiement
        fields = ['montantD','descriptionD']
    
    
class LocationForm(ModelForm):
    
    dateDebut = forms.DateField(label="Date debut bail (mm/dd/yyyy):",widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    dateFin = forms.DateField(label="Date fin bail (mm/dd/yyyy):",widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))

    class Meta:
        model = Location
        fields=['dateDebut','dateFin']


class UpdateBail(ModelForm):
    dateFin = forms.DateField(label="Date fin bail (mm/dd/yyyy):",widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    
    
class LocationForm(ModelForm):
    dateDebut = forms.DateField(label="Date debut bail (mm/dd/yyyy):",widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    dateFin = forms.DateField(label="Date fin bail (mm/dd/yyyy):",widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    
    class Meta:
        model = Location
        fields=['dateDebut','dateFin']