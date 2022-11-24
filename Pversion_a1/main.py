#!/usr/bin/python3

#Schneider Gabriel / 15-08-2022
#Zufall für Loot


from random import randint
import tkinter as tk

import loot
import mod 

####################################################################
debug = False

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
Item = None

####################################################################
#definitionen
def Loot_main():
    zufall_mainquali= randint(1,20) #Entscheidung der Ersten Qualitätsstufe
    
    def Mod():      #Globalisierung aller Nötien variablen
        global modsvar
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
        global Item
        global mods
        
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

####################################################################
#Item Configs
        
        ItemL.config(text=item, bg="grey")
        try:
            Mod1.config(text=mods[0], bg="grey")
        except IndexError:
            Mod1.config(text=" ", bg="grey")
        try:
            Mod2.config(text=mods[1], bg="grey")
        except IndexError:
            Mod2.config(text=" ", bg="grey") 
        try:
            Mod3.config(text=mods[2], bg="grey")
        except IndexError:
            Mod3.config(text=" ",bg="grey") 
        try:
            Mod4.config(text=mods[3], bg="grey")
        except IndexError:
            Mod4.config(text=" ", bg="grey") 
        
####################################################################
# Main Qualität        
        
    if zufall_mainquali == 20:
        erg_schrott = randint(0,count_schrott)
        item = loot.schrott[erg_schrott]
        
        Mod()
                
    elif zufall_mainquali <= 19 and zufall_mainquali >= 10:
        erg_normal = randint(0,count_normal)
        item = loot.normal[erg_normal]
        
        Mod()
        
    elif zufall_mainquali <= 9 and zufall_mainquali >= 5:
        erg_selten = randint(0,count_selten)
        item = loot.selten[erg_selten]
        
        Mod()
        
    elif zufall_mainquali <= 4 and zufall_mainquali >= 2:
        erg_sehr_selten = randint(0,count_sehr_selten)
        item = loot.sehr_selten[erg_sehr_selten]
        
        Mod()
        
    elif zufall_mainquali == 1:
        erg_epic = randint(0,count_epic)
        item = loot.epic[erg_epic]
            
        Mod()
    
    if debug == True:
        print("")
        print(item)
        print(mods)
        
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

####################################################################
#Bereich für zufälle

#Zufalls Fenster Titel    
title = ["Loot für Phex!",
         "Looten und Leveln!",
         "Get this you Thief!",
         "Da hat wer was fallen lassen!"]
count_title = len(title) -1
zufall_titel = randint(0, count_title)
titel_text = title[zufall_titel]

#Zufalls Knopf Text
knopf = ["Drücken für Loot!",
         "Klicken für Items",
         "Kiste öffnen",
         "GESCHENKE!",
         "Beutel Schneiden!"]
count_knopf = len(knopf) -1
zufall_knopf = randint(0,count_knopf)
knopf_text = knopf[zufall_knopf]

####################################################################
#Fenster aufbau und aussehen
root = tk.Tk()
root.title(titel_text)
root.geometry("300x300")
root.minsize(width= 300, height= 300)
root.config(bg="grey")

Label1 = tk.Label(root, text= "Würfel mich!", font=25)
Label1.configure(bg="grey")
Label1.pack( fill="y", side="top", padx=20, pady=20)

ItemL = tk.Label(root, text=Item)
ItemL.configure(bg="grey")
ItemL.pack()

Mod1 = tk.Label(root)
Mod1.configure(bg="grey")
Mod1.pack()

Mod2 = tk.Label(root)
Mod2.configure(bg="grey")
Mod2.pack()

Mod3 = tk.Label(root)
Mod3.configure(bg="grey")
Mod3.pack()

Mod4 = tk.Label(root)
Mod4.configure(bg="grey")
Mod4.pack()

Button1 =tk.Button(root, text= knopf_text, command=Loot_main, font=20)
Button1.configure(bg="grey")
Button1.pack(side="bottom", ipadx=20, ipady=20)


root.mainloop()