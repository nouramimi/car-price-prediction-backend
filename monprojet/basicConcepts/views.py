from django.shortcuts import render
#from django.http import HttpResponse
import pickle 
def welcome(request ):
    #return HttpResponse("hello world")
    return render(request,"index.html")

def User(request):
    username= request.GET["username"]
    #print(username)
    #pass the name into the web page
    return render(request,"user.html",{"name" : username})


def home(request ):
    #return HttpResponse("hello world")
    return render(request,"main.html")

def result(request):
    if request.method == 'GET':
        Marque = request.GET.get("marque")
        Modèle = request.GET.get("modele")
        Énergie = request.GET.get("carburant")
        mise_en_circulation = int(request.GET.get("mise_en_circulation"))
        Puissance_fiscale = int(request.GET.get("Puissance_fiscale"))
        Kilométrage = float(request.GET.get("kilometrage"))
        Carrosseie = request.GET.get("Carrosseie")
        cylindre = int(request.GET.get("cylindre"))
        Transmission = request.GET.get("Transmission")
        
        result = getPredictions(Marque, Modèle, Puissance_fiscale, Transmission, Kilométrage, mise_en_circulation, Carrosseie, cylindre, Énergie)

        return render(request, "result.html", {"result": result})

#def getPredictions(marque,modele,carburant,boiteVitesse,mise_en_circulation,kilometrage):
    #model=pickle.load(open("ml_model.sav","rb") )
    #scaled=pickle.load(open("acaler.sav","rb") )
    #prediction =model.predict(scaled.transform([
    #  marque,modele,carburant,boiteVitesse,mise_en_circulation,kilometrage
    #]))
    #return prediction

import pickle

def getPredictions(Marque, 	Modèle,Puissance_fiscale,Transmission,Kilométrage, mise_en_circulation,Carrosserie, kilometrage,cylindre	,Énergie):
    # Charger le modèle depuis le fichier pickle
    with open("modele.pkl", "rb") as f:
        model = pickle.load(f)
    
    # Effectuer les prétraitements nécessaires sur les données d'entrée
    data = [[Marque,Modèle,Puissance_fiscale,Transmission,Kilométrage, mise_en_circulation,Carrosserie, kilometrage,cylindre	,Énergie]]
    
    # Effectuer des prédictions avec le modèle chargé
    prediction = model.predict(data)
    
    return prediction

