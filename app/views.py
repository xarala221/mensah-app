from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import date


# Create your views here.

def home(request):    
    return render(request,"index.html",locals())
    
@login_required(login_url="/login/")    
def maison_list(request):
    user = request.user
    maisons = Maison.objects.filter(numP=user)
    return render(request, "mon_bien/maison_list.html", {"maisons": maisons})


@login_required(login_url="/login/")
def new_maison(request):
    form = MaisonForm(request.POST or None, request.FILES or None)
    numP = request.user
    if form.is_valid():
        form.save(commit=False)
        nomM = form.cleaned_data.get("nomM")
        numRueM = form.cleaned_data.get("numRueM")
        adresseM = form.cleaned_data.get("adresseM")
        codePostalM = form.cleaned_data.get("codePostalM")
        photoM1 = form.cleaned_data.get("photoM1")
        photoM2 = form.cleaned_data.get("photoM2")
        photoM3 = form.cleaned_data.get("photoM3")
        villeM = form.cleaned_data.get("villeM")  
        maison = Maison.objects.create(
        nomM = nomM,
        numRueM = numRueM,
        adresseM = adresseM,
        codePostalM = codePostalM,
        villeM = villeM,
        numP = numP,
        photoM1 = photoM1,
        photoM2 = photoM2,
        photoM3 = photoM3
        )
        maison.save()
        
        return redirect("/maisons/")
    
    return render(request, "mon_bien/new_maison.html",locals())


@login_required(login_url="/login/")
def new_logement(request, numM):
    form = LogementForm(request.POST or None, request.FILES or None)
    maison = get_object_or_404(Maison, pk= numM)
    if form.is_valid():
        form.save(commit=False)
        superficie = form.cleaned_data.get("superficie")
        loyer = form.cleaned_data.get("loyer")        
        typeL = form.cleaned_data.get("typeL")
        photoL1 = form.cleaned_data.get("photoL1")
        photoL2 = form.cleaned_data.get("photoL2")
        photoL3 = form.cleaned_data.get("photoL3")
        
        logement = Logement.objects.create(
            typeL = typeL,
            superficie = superficie,
            loyer = loyer,
            numM = maison,
            photoL1 = photoL1,
            photoL2 = photoL2,
            photoL3 = photoL3
        )
        logement.save()
        
        return redirect("/maisons/"+str(numM)+"/details/")
    
    return render(request, "mon_bien/maison/new_logement.html",locals())

@login_required(login_url="/login/")
def maison_detail(request,numM):
    maison = get_object_or_404(Maison, pk= numM)
    logements = Logement.objects.filter(numM=maison)                
    return render(request, "mon_bien/maison/maison_details.html",locals());

@login_required(login_url="/login/")
def update_delete_maison(request,numM):
    maison = get_object_or_404(Maison, pk= numM)
    return render(request, "mon_bien/maison/update_delete_maison.html",locals());

@login_required(login_url="/login/")
def delete_maison(request, numM):

    maison = get_object_or_404(Maison, pk=numM)
    if request.method == "POST":
        maison.delete()
        return redirect("/maisons/")
    return render(request, "mon_bien/maison/update_delete_maison/delete_maison.html", locals())

@login_required(login_url="/login/")
def update_maison(request, numM):
    maison = get_object_or_404(Maison, pk=numM)
    form = MaisonForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save(commit=False)
        nomM = form.cleaned_data.get("nomM")
        numRueM = form.cleaned_data.get("numRueM")
        adresseM = form.cleaned_data.get("adresseM")
        codePostalM = form.cleaned_data.get("codePostalM")
        photoM1 = form.cleaned_data.get("photoM1")
        photoM2 = form.cleaned_data.get("photoM2")
        photoM3 = form.cleaned_data.get("photoM3")
        villeM = form.cleaned_data.get("villeM")  
        Maison.objects.filter(pk=numM).update(
        nomM = nomM,
        numRueM = numRueM,
        adresseM = adresseM,
        codePostalM = codePostalM,
        villeM = villeM,
        photoM1 = photoM1,
        photoM2 = photoM2,
        photoM3 = photoM3
        )
                
        return redirect("/maisons/"+str(numM)+"/details")
    
    return render(request, "mon_bien/maison/update_delete_maison/update_maison.html",locals())
    

@login_required(login_url="/login/")
def maison_depense(request, numM):
    user = request.user
    form = DepenserForm(request.POST or None)
    maison = get_object_or_404(Maison, pk= numM)
    logements = Logement.objects.filter(numM=maison)
    if form.is_valid():
        form.save(commit=False)
        montantD = form.cleaned_data.get("montantD")
        montantD = montantD / len(logements)
        descriptionD = form.cleaned_data.get("descriptionD")
        for logement in logements:
            depense = Depenser.objects.create(
                numP=user,
                numLogement = logement,
                montantD = montantD,
                descriptionD = descriptionD
                
            )
            depense.save()
        return redirect("/maisons/"+str(numM)+"/details/")
    return render(request, "mon_bien/maison/depense_maison.html",locals())



@login_required(login_url="/login/")
def locataire_list(request):
    user = request.user
    locataires = Locataire.objects.filter(created_by=user)
    locations = []
    for locataire in locataires:
        locationObjects = Location.objects.filter(numLocataire=locataire)
        for locationObject in locationObjects:
            locations.append(locationObject)    
    return render(request,"Locataire/locataire_list.html",locals())


@login_required(login_url="/login/")
def paiement(request, numLogement, numLocataire):
    numLogement = get_object_or_404(Logement, pk= numLogement)
    numLocataire = get_object_or_404(Locataire, pk= numLocataire)
    form = PaiementForm(request.POST or None)
    if form.is_valid():
        form.save(commit=False)
        montantP = form.cleaned_data.get('montantP')  
        
        paiement = Paiement.objects.create(
            numLocataire = numLocataire,
            numLogement = numLogement,
            montantP = montantP
        )
        paiement.save()
        return redirect("/maisons/logements/"+str(numLogement.numLogement)+"/details/")
    
    return render(request, "mon_bien/maison/logement/paiement.html",locals())

@login_required(login_url="/login/")
def logement_detail(request, numM, numLogement):
    logement = get_object_or_404(Logement, pk= numLogement)
    paiements =  Paiement.objects.filter(numLogement=logement)
    depenses = Depenser.objects.filter(numLogement = logement)
    locataire = None
    location = None
    locations = Location.objects.filter(numLogement=logement)
    if(locations):
        for l in locations:
            date = l.dateFin
            d = datetime(date.year,date.month,date.day)
            now = datetime.now()
            if (d > now):
                locataire = l.numLocataire
                location = l
                                
    return render(request, "mon_bien/maison/logement/logement_details.html",locals())

@login_required(login_url="/login/")
def logement_depense(request, numLogement):
    user = request.user
    form = DepenserForm(request.POST or None)
    logement = get_object_or_404(Logement, pk= numLogement)
    if form.is_valid():
        form.save(commit=False)
        montantD = form.cleaned_data.get("montantD")
        descriptionD = form.cleaned_data.get("descriptionD")
        depense = Depenser.objects.create(
                numP=user,
                numLogement = logement,
                montantD = montantD,
                descriptionD = descriptionD
                
        )
        depense.save()
        return redirect("/maisons/"+str(logement.numM.numM)+"/logements/"+str(numLogement)+"/details/")
    return render(request, "mon_bien/maison/logement/depense_logement.html",locals())    


@login_required(login_url="/login/")
def update_delete_logement(request, numM, numLogement):
    logement = get_object_or_404(Logement, pk= numLogement)
    return render(request,"mon_bien/maison/logement/update_delete_logement.html",locals())


@login_required(login_url="/login/")
def update_logement(request, numM, numLogement):
    logement = get_object_or_404(Logement, pk=numLogement)
    form = LogementForm(request.POST or None, request.FILES or None)
    maison = get_object_or_404(Maison, pk= numM)
    if form.is_valid():
        form.save(commit=False)
        superficie = form.cleaned_data.get("superficie")
        loyer = form.cleaned_data.get("loyer")        
        typeL = form.cleaned_data.get("typeL")
        photoL1 = form.cleaned_data.get("photoL1")
        photoL2 = form.cleaned_data.get("photoL2")
        photoL3 = form.cleaned_data.get("photoL3")
        
        Logement.objects.filter(pk=numLogement).update(
            typeL = typeL,
            superficie = superficie,
            loyer = loyer,
            numM = maison,
            photoL1 = photoL1,
            photoL2 = photoL2,
            photoL3 = photoL3
        )       
        return redirect("/maisons/"+str(numM)+"/logements/"+str(numLogement)+"/details/")
    
    return render(request, "mon_bien/maison/logement/update_delete_logement/update_logement.html",locals())


@login_required(login_url="/login/")
def delete_logement(request, numM, numLogement):
    logement = get_object_or_404(Logement, pk=numLogement)
    if request.method == "POST":
        logement.delete()
        return redirect("/maisons/"+str(numM)+"/details/")
    return render(request, "mon_bien/maison/logement/update_delete_logement/delete_logement.html", locals())


@login_required(login_url="/login/")
def update_date_fin_bail(request, idLocation):
    location = get_object_or_404(Location, pk = idLocation)
    return render(request,'mon_bien/maison/logement/update_date_fin_bail.html',locals())


@login_required(login_url="/login/")
def add_locataire(request, numM, numLogement):

    logement = get_object_or_404(Logement, pk= numLogement)

    form = LocataireForm(request.POST or None)
    locataire = None
    if form.is_valid():
        form.save(commit=False)
        user = request.user
        nomLocataire = form.cleaned_data.get("nomLocataire")
        prenomLocataire = form.cleaned_data.get("prenomLocataire")
        telephoneLocataire = form.cleaned_data.get("telephoneLocataire")
        emailLocataire = form.cleaned_data.get("mailLocataire")
        profession = form.cleaned_data.get('profession')
        locataire = Locataire.objects.create(
            nomLocataire = nomLocataire,
            prenomLocataire = prenomLocataire,
            telephoneLocataire = telephoneLocataire,
            mailLocataire = emailLocataire,
            profession = profession,
            created_by = user
        )
        locataire.save()
        
        return redirect("/maisons/"+str(numM)+"/logements/"+str(numLogement)+"/"+str(locataire.numLocataire)+"/bail", locals() )    

    return render(request, "mon_bien/maison/logement/add_locataire.html",locals())

@login_required(login_url="/login/")
def create_bail(request, numM, numLogement, numLocataire):
    logement = get_object_or_404(Logement, pk= numLogement)
    locataire = get_object_or_404(Locataire, pk= numLocataire)
    erreur = False
 
    form = LocationForm(request.POST or None)
    if form.is_valid():
        form.save(commit=False)
        dateDebut = form.cleaned_data.get('dateDebut')
        dateFin = form.cleaned_data.get('dateFin')
        if( dateDebut > dateFin):
            erreur = True
            return render(request, "mon_bien/maison/logement/bail.html",locals())
        location = Location.objects.create(
            numLocataire = locataire,
            numLogement = logement,
            dateDebut = dateDebut,
            dateFin = dateFin
        )
        location.save()
        
        return redirect("/maisons/"+str(numM)+"/logements/"+str(numLogement)+"/details/",locals())
    
    return render(request, "mon_bien/maison/logement/bail.html",locals())
    
    
    
@login_required(login_url="/login/") 
def stop_bail(request, idLocation):
    location = get_object_or_404(Location, pk= idLocation)
   
    if request.method == "POST":
        Location.objects.filter(pk=idLocation).update(
            dateFin = datetime.now()
        )
             
        return redirect("/maisons/"+str(location.numLogement.numM.numM)+"/logements/"+str(location.numLogement.numLogement)+"/details/")
    
    return render(request, "mon_bien/maison/logement/update_date_fin_bail/stop_bail.html",locals())


@login_required(login_url="/login/")
def updateBail(request, idLocation):
    location = get_object_or_404(Location, pk = idLocation)
    erreur = False
    form = LocationForm(request.POST or None)
    if form.is_valid():
        form.save(commit=False)
        dateDebut = form.cleaned_data.get('dateDebut')
        dateFin = form.cleaned_data.get('dateFin')
        if( dateDebut > dateFin):
            erreur = True
            return (request, 'mon_bien/maison/logement/update_date_fin_bail/update_bail.html', locals())
        Location.objects.filter(pk=idLocation).update(
            dateDebut = dateDebut,
            dateFin = dateFin
        )
        return redirect("/maisons/"+str(location.numLogement.numM.numM)+"/logements/"+str(location.numLogement.numLogement)+"/details/")
    
    return render(request, 'mon_bien/maison/logement/update_date_fin_bail/update_bail.html', locals())