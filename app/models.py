from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

# Create your models here.

class Maison(models.Model):
    numM = models.AutoField(primary_key=True)
    nomM = models.CharField(max_length = 150, blank=True)
    numRueM = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(19999999999)])
    adresseM = models.CharField(max_length = 150)
    codePostalM = models.CharField(max_length = 5)
    villeM = models.CharField(max_length = 150)
    numP = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def upload_path(self, filename):
        return 'media/%s_%s' % (self.created_at.strftime("%Y%m%d_%H%M%S"), filename)
    
    photoM1 = models.FileField(upload_to=upload_path, blank = True, null=True, default='img/show.jpg')
    photoM2 = models.FileField(upload_to=upload_path, blank = True, null=True)
    photoM3 = models.FileField(upload_to=upload_path, blank = True, null=True)    
    def __str__(self):
        return f"{self.numRueM} {self.adresseM} {self.villeM}"
    
    class Meta:
        db_table = 'maison'
    
    


class Logement(models.Model):
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
    
    numLogement = models.AutoField(primary_key=True)
    typeL = models.CharField(max_length=200, choices=TYPE_CHOICES)
    superficie = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(19999999999)])
    loyer = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(19999999999)])
    numM = models.ForeignKey(Maison, on_delete=models.CASCADE, db_column='numM')
    created_at = models.DateTimeField(auto_now_add=True)  
    def upload_path(self, filename):
        return 'media/%s_%s' % (self.created_at.strftime("%Y%m%d_%H%M%S"), filename)
    
    photoL1 = models.FileField(upload_to=upload_path, blank = True, null=True)
    photoL2 = models.FileField(upload_to=upload_path, blank = True, null=True)
    photoL3 = models.FileField(upload_to=upload_path, blank = True, null=True)
    
    def __str__(self):
        return f"chambre: {self.numLogement} | {self.numM.numRueM} {self.numM.adresseM} {self.numM.villeM}"
    class Meta:
        db_table = 'logement'
        
class Depenser(models.Model):
    numP = models.ForeignKey(User, on_delete=models.CASCADE)
    numLogement = models.ForeignKey(Logement, on_delete=models.CASCADE, db_column='numLogement')
    montantD = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(19999999999)])
    dateD = models.DateTimeField(auto_now_add=True)
    descriptionD = models.CharField(max_length = 300)

    def __str__(self):
        return f"Chambre : {self.numLogement.numLogement} | Maison : {self.numLogement.numM.numRueM} {self.numLogement.numM.adresseM} {self.numLogement.numM.villeM} | Date : {self.dateD} | Montant : {self.montantD}"
    
    class Meta:
        db_table = 'depenser'
        
class Locataire(models.Model):
    numLocataire = models.AutoField(primary_key=True)
    nomLocataire = models.CharField(max_length = 150) 
    prenomLocataire = models.CharField(max_length = 150)
    telephoneLocataire = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(19999999999)])
    mailLocataire = models.EmailField(max_length = 150)
    profession = models.CharField(max_length = 150)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Nom: {self.nomLocataire} {self.prenomLocataire} | {self.profession}"
       
    class Meta:
        db_table = 'locataire'

class Location(models.Model):
    idLocation = models.AutoField(primary_key=True)
    numLocataire = models.ForeignKey(Locataire, on_delete=models.CASCADE, db_column='numLocataire')
    numLogement = models.ForeignKey(Logement, on_delete=models.CASCADE, db_column='numLogement')
    dateDebut = models.DateField(auto_now=False, auto_now_add=False)
    dateFin = models.DateField( auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return f"Chambre :{self.numLogement} {self.dateDebut} - {self.dateFin}"
       
    class Meta:
        db_table = 'location'
        
class Paiement(models.Model):
    idPaiement = models.AutoField(primary_key=True)
    numLocataire = models.ForeignKey(Locataire, on_delete=models.CASCADE, db_column='numLocataire')
    numLogement = models.ForeignKey(Logement, on_delete=models.CASCADE, db_column='numLogement')
    montantP = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(19999999999)])
    datePaie = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"idPaiement: {self.idPaiement} | {self.datePaie} {self.montantP}"
   
    class Meta:
        db_table = 'paiement'
        
        
