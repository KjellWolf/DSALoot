#!/usr/bin/python3

#Schneider Gabriel / 15-08-2022
#Zufall für Loot


from random import randint
import tkinter as tk
import webbrowser

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
verwesung = None


####################################################################
#definitionen

#Auslöser zum öffnen eines Browsers für das Support Label
def callback(url):
    webbrowser.open_new(url)

#Auslöser der Hauptqualität und sddarunter folgenden Modifikatoren
def Loot_main():
    
    #Entscheidung der Ersten Qualitätsstufe
    
    #Angeben Einer erschwernis oder erleichterung im Erschwernis Entry
    erschwernis = 0
    erschwernis = erschwernisb.get()
    try:
        erschwernis = int(erschwernis)
    except ValueError:
        erschwernis = 0
    
    #Auswürfeln der Main Qualität verrechnet mit der erschwernis
    zufall_mainquali= randint(1,20)
    zufall_mainquali = zufall_mainquali + erschwernis
    
   
####################################################################
#Definition des abfragen der Modifikatoren mit globalisierung    
    def Mod():      
        
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
        global Item
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

####################################################################
#Item und Mod Configs zur textzuweisung für jedes drücken
        #Item
        ItemL.config(text=item, bg=backgroud)
        
        #Mod1
        try:
            Mod1.config(text=mods[0], bg=backgroud)
        except IndexError:
            Mod1.config(text=" ", bg=backgroud)
        
        #Mod2
        try:
            Mod2.config(text=mods[1], bg=backgroud)
        except IndexError:
            Mod2.config(text=" ", bg=backgroud) 
        
        #Mod3
        try:
            Mod3.config(text=mods[2], bg=backgroud)
        except IndexError:
            Mod3.config(text=" ",bg=backgroud) 
        
        #Mod4
        try:
            Mod4.config(text=mods[3], bg=backgroud)
        except IndexError:
            Mod4.config(text=" ", bg=backgroud) 
        
####################################################################
# Main Qualität        
        
    if zufall_mainquali >= 20:
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
        
    elif zufall_mainquali <= 1:
        erg_epic = randint(0,count_epic)
        item = loot.epic[erg_epic]
        Mod()

####################################################################
#Debug an und aus
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

####################################################################
#Bereich für zufälle

#Zufalls Fenster Titel und versionsnummer   
title = ["Loot für Phex!",
         "Looten und Leveln!",
         "Get this you Thief!",
         "Nimm oder Stirb"]
count_title = len(title) -1
zufall_titel = randint(0, count_title)
titel_text = "V_a.2 " + title[zufall_titel] 

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
#aussehen Parameter

#schriften
überschrift  = "Arial", 25
subüberschrift = "Arial", 17, "underline"
schrift      = "Arial", 15
knopfschrift = "Arial", 30
subschrift   = "Arial", 10, "underline"

#farben
backgroud = "#719DB0"
button_press = "#61808D"
####################################################################
#Fenster aufbau und aussehen

root = tk.Tk()              #Hauptfenster Bestimmen
root.title(titel_text)      #Fenster Titel Setzen über "titel_text"
root.iconbitmap('Python/Loot/version_a.2/Dateien/Dice20.ico')  #Fenster Icon setzen
root.geometry("420x450")    #Fenster Startgröße setzen in pixel
root.resizable(False,   
               False)       #Fenster größe festsetzen
root.config(bg=backgroud)   #Fenster hintergund setzen über "background"

#Überschrift
Fenster_überschrift = tk.Label(root,    #verknüpfung zum hauptfenster
                  text= "Lass die Würfel Rollen",   #überschirft Fenstertext
                  font=(überschrift),   #Texteinstellungen über "überschrift"
                  bd=4,                 #Rand Dicke
                  relief="ridge")       #Rand art
Fenster_überschrift.configure(bg=backgroud) 
Fenster_überschrift.pack( fill="both",
            side="top",
            ipadx=20,
            ipady=10)

#Item Label unter überschrift
ItemL = tk.Label(root,      #verknüpfung zum hauptfenster
                 text=Item,
                 font=(subüberschrift))
ItemL.configure(bg=backgroud)
ItemL.pack(ipady=15)

#Modifikator 1 unter Items
Mod1 = tk.Label(root,       #verknüpfung zum hauptfenster
                font=(schrift))
Mod1.configure(bg=backgroud)
Mod1.pack()

#Modifikator 2 unter Modifikator 1
Mod2 = tk.Label(root,       #verknüpfung zum hauptfenster
                font=(schrift))
Mod2.configure(bg=backgroud)
Mod2.pack()

#Modifikator 3 unter Modifikator 2
Mod3 = tk.Label(root,       #verknüpfung zum hauptfenster
                font=(schrift))
Mod3.configure(bg=backgroud)
Mod3.pack()

#Modifikator 4 unter Modifikator 3
Mod4 = tk.Label(root,   #verknüpfung zum hauptfenster
                font=(schrift))
Mod4.configure(bg=backgroud)
Mod4.pack()

#Support Label unter Loot_gen knopf
Support = tk.Label(root,    #verknüpfung zum hauptfenster
                  text="Discord für Support und Ideen",
                  font=(subschrift),
                  cursor="hand2")
Support.configure(bg=backgroud)
Support.pack( fill="y",
            side="bottom",
            ipadx=3,
            ipady=5)
Support.bind("<Button-1>", lambda e: callback("https://discord.gg/58HCd8NHuX"))

#Loot_gen knopf unter Erschwernes Entry
Loot_gen =tk.Button(root,   #verknüpfung zum hauptfenster
                   text= knopf_text,
                   command=Loot_main,
                   font=(knopfschrift),
                   height=1,
                   width=120,
                   bd=7,
                   relief="groove")
Loot_gen.configure(bg=backgroud,
                  activebackground=button_press)
Loot_gen.pack(side="bottom",
             ipadx=2,
             ipady=0,
             padx=30,
             pady=3)

#Erschwernis Entry über Loot_gen knopf
erschwernisb = tk.Entry(root,   #verknüpfung zum hauptfenster
                        width=7,)
erschwernisb.configure()
erschwernisb.insert(0, "Erschw.")
erschwernisb.pack(side="bottom")

root.mainloop()