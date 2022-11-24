#!/usr/bin/python3

#Schneider Gabriel / 15-08-2022
#Zufall für Loot


from random import randint
import webbrowser

import lootliste as loot
import lootmods as mod



####################################################################
debug = True

####################################################################
#Setzen erster Variablen
modsvar = None
quali = None
modsvar = None
farbe = None
farbe_k = None
anzahl_ran = None
portionen_ran = None
füllstand = None
seite = None
gott = None
gott_tier = None
farbe_zusatz = None
metall_zusatz = None
item = None
verwesung = None


####################################################################
#definitionen
####################################################################
#Definition des abfragen der Modifikatoren mit globalisierung    
def Mod(item):      
        
    global modsvar #Globalisierung aller Nötigen variablen
    global quali
    global farbe
    global farbe_zusatz
    global farbe_k
    global anzahl_ran
    global portionen_ran
    global füllstand
    global seite
    global gott
    global gott_tier
    global metall_zusatz
    global mods
    global verwesung
     
####################################################################
#Setzen einer Leeren Liste
    mods = []
        
####################################################################
 #Modifikationen       
    #Zufall der Quaität der Items
    if item in loot.quali:
        quali_ran = randint(0,count_quali)
        quali = mod.quali[quali_ran]
        quali = ["Qualität: ", quali]
        quali = ' '.join(quali)
        mods.append(quali)

    #Zufall der Farbe mit zusatz für Items
    if item in loot.farbe:
        farbe_ran = randint(0,count_farbe)
        farbe = mod.farbe[farbe_ran]
            
        farbe_zusatz_ran = randint(0,count_farbe_zusatz)
        farbe_zusatz = mod.farbe_zusatz[farbe_zusatz_ran]
        farbe_k = ["Farbe:", farbe_zusatz, farbe]
        farbe_k = ' '.join(farbe_k)
            
        mods.append(farbe_k)

        #zufall der Anzahl von Items
    if item in loot.anzahl:
        anzahl_ran = randint(1,25)
        anzahl_ran = str(anzahl_ran)
        anzahl_ran = ["Anzahl:", anzahl_ran]
        anzahl_ran = ' '.join(anzahl_ran)
        mods.append(anzahl_ran)

        #Zufall der Portionen von Items
    if item in loot.portionen:
        portionen_ran = randint(1,30)
        portionen_ran = str(portionen_ran)
        portionen_ran = ["Portionen: ", portionen_ran]
        portionen_ran = ' '.join(portionen_ran)
        mods.append(portionen_ran)
            
        #Zufall des Füllstands eines Items
    if item in loot.füllstand:
        füllstand_ran = randint(0,count_füllstand)
        füllstand = mod.füllstand[füllstand_ran]
        füllstand = ["Füllstand: ", füllstand]
        füllstand = ' '.join(füllstand)  
        mods.append(füllstand)
            
        #Zufall der Seite (Liks, Rechts, Beide)
    if item in loot.seite:
        seite_ran = randint(0,count_seite)
        seite = mod.seite[seite_ran]
        seite = ["Seite: ", seite]
        seite = ' '.join(seite)
        mods.append(seite)
        
        #Zufalls des Metall zustands für Items
    if item in loot.metall_zusatz:
        metall_zusatz_ran = randint(0,count_metall_zusatz)
        metall_zusatz = mod.metall_zusatz[metall_zusatz_ran]
        metall_zusatz = ["Metall zustand: ", metall_zusatz]
        metall_zusatz = ' '.join(metall_zusatz)
        mods.append(metall_zusatz)
        
        #Zufall für die Glaubenszuordnung für Items
    if item in loot.gott:
        gott_ran = randint(0,count_gott)
        gott = mod.gott[gott_ran]
        gott = ["Glaubenszuordnung: ", gott]
        gott = ' '.join(gott)
        mods.append(gott)
        
        #Zufall für das Glaubenstier für Items
    if item in loot.gott_tier:
        gott_tier_ran = randint(0,count_gott_tier)
        gott_tier = mod.gott_tier[gott_tier_ran]
        gott_tier = ["Glaubenstier :", gott_tier]
        gott_tier = ' '.join(gott_tier)
        mods.append(gott_tier)
        
        #Zufall für Verwesung
    if item in loot.verwesung:
        verwesung_ran = randint(0,count_verwesung)
        verwesung = mod.verwesung[verwesung_ran]
        verwesung = ["Zustand: ", verwesung]
        verwesung = ' '.join(verwesung)
        mods.append(verwesung)   

    return mods

#Auslöser zum öffnen eines Browsers für das Support Label
def callback(url):
    webbrowser.open_new(url)

#Auslöser der Hauptqualität und sddarunter folgenden Modifikatoren
def Loot_main(erschwernis):
    #Entscheidung der Ersten Qualitätsstufe
    global zufall_mainquali
    #Angeben Einer erschwernis oder erleichterung im Erschwernis Entry
  
    try:
        erschwernis = int(erschwernis)
    except ValueError:
        erschwernis = 0
    
    
    #Auswürfeln der Main Qualität verrechnet mit der erschwernis
    zufall_mainquali= randint(1,20)
    zufall_mainquali = zufall_mainquali + erschwernis
        
####################################################################
# Main Qualität        
        
    if zufall_mainquali >= 20:
        erg_schrott = randint(0,count_schrott)
        item = loot.schrott[erg_schrott]
             
    elif zufall_mainquali <= 19 and zufall_mainquali >= 10:
        erg_normal = randint(0,count_normal)
        item = loot.normal[erg_normal]

    elif zufall_mainquali <= 9 and zufall_mainquali >= 5:
        erg_selten = randint(0,count_selten)
        item = loot.selten[erg_selten]
 
        
    elif zufall_mainquali <= 4 and zufall_mainquali >= 2:
        erg_sehr_selten = randint(0,count_sehr_selten)
        item = loot.sehr_selten[erg_sehr_selten]
             
    elif zufall_mainquali <= 1:
        erg_epic = randint(0,count_epic)
        item = loot.epic[erg_epic]
              
    return item 
    
####################################################################
#Debug an und aus
def Debug():
    if debug == True:
        print("")
        print("Items: ",item)
        print("Modifikatoren: ", mods)
        print("Main Quali: ", zufall_mainquali)
####################################################################
#Listenlängen
count_schrott = len(loot.schrott) -1
count_normal = len(loot.normal) -1
count_selten = len(loot.selten) -1
count_sehr_selten = len(loot.sehr_selten) -1
count_epic = len(loot.epic) -1

count_quali = len(mod.quali) -1
count_farbe = len(mod.farbe) -1
count_farbe_zusatz = len(mod.farbe_zusatz) -1
count_füllstand = len(mod.füllstand) -1
count_seite = len(mod.seite) -1
count_metall_zusatz = len(mod.metall_zusatz) -1
count_gott = len(mod.gott) -1
count_gott_tier = len(mod.gott_tier) -1 
count_verwesung =len(mod.verwesung) -1