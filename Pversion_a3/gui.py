#!/usr/bin/python3

#Schneider Gabriel / 15-08-2022
#Zufall für Loot

from random import randint
from tkinter import ttk
import tkinter as tk

import lootlogic as ll 
import encounterlogic as el

#funktion Loot
def DSALoot():
        #Item
        erschwernis = 0
        erschwernis = erschwernisb.get()
        item = ll.Loot_main(erschwernis)
        mods = ll.Mod(item)
        
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

def Ereignis():
    ort = select_ort.get()
    Ort_über.config(text=ort, bg=backgroud)
    
    begegnung = None
    
    if ort == el.namen_main[0]:
        begegnung = el.Stadt()
    if ort == el.namen_main[1]:
        begegnung = el.Landstr()
    if ort == el.namen_main[2]:
        begegnung = el.Dorf()
    if ort == el.namen_main[3]:
        begegnung = el.Wald()
    if ort == el.namen_main[4]:
        begegnung = el.üNachtW()
    if ort == el.namen_main[5]:
        begegnung = el.inTavern()
    
    Ort_begeg_n.config(text=begegnung[0], bg=backgroud)
    Ort_begeg.config(text=begegnung[1], bg=backgroud)
        
    print(ort)
    
####################################################################
#Bereich für zufälle

#Zufalls Fenster Titel und versionsnummer   
title = ["Loot für Phex!",
         "Looten und Leveln!",
         "Get this you Thief!",
         "Nimm oder Stirb"]
count_title = len(title) -1
zufall_titel = randint(0, count_title)
titel_text = "V_a.3 " + title[zufall_titel] 

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
#root.iconbitmap('Python\Loot\Pversion_a3\Dateien\Fox.ico')  #Fenster Icon setzen
root.geometry("420x500")    #Fenster Startgröße setzen in pixel
root.resizable(False,   
               False)       #Fenster größe festsetzen
root.config(bg=backgroud)   #Fenster hintergund setzen über "background"

#style




tabs = ttk.Notebook(root)
tabs.pack(expand=True, ipady=30)


lootf = tk.Frame(root, bg=backgroud)
lootf.config(bg=backgroud)
lootf.pack(expand=True)
tabs.add(lootf, text="Loot Generator")

#Überschrift
Fenster_überschrift = tk.Label(lootf,    #verknüpfung zum hauptfenster
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
ItemL = tk.Label(lootf,      #verknüpfung zum hauptfenster
                 text=ll.item,
                 font=(subüberschrift))
ItemL.configure(bg=backgroud)
ItemL.pack(ipady=15)

#Modifikator 1 unter Items
Mod1 = tk.Label(lootf,       #verknüpfung zum hauptfenster
                font=(schrift))
Mod1.configure(bg=backgroud)
Mod1.pack()

#Modifikator 2 unter Modifikator 1
Mod2 = tk.Label(lootf,       #verknüpfung zum hauptfenster
                font=(schrift))
Mod2.configure(bg=backgroud)
Mod2.pack()

#Modifikator 3 unter Modifikator 2
Mod3 = tk.Label(lootf,       #verknüpfung zum hauptfenster
                font=(schrift))
Mod3.configure(bg=backgroud)
Mod3.pack()

#Modifikator 4 unter Modifikator 3
Mod4 = tk.Label(lootf,   #verknüpfung zum hauptfenster
                font=(schrift))
Mod4.configure(bg=backgroud)
Mod4.pack()

#Support Label unter Loot_gen knopf
Support = tk.Label(lootf,    #verknüpfung zum hauptfenster
                  text="Discord für Support und Ideen",
                  font=(subschrift),
                  cursor="hand2")
Support.configure(bg=backgroud)
Support.pack( fill="y",
            side="bottom",
            ipadx=3,
            ipady=5)
Support.bind("<Button-1>", lambda e: ll.callback("https://discord.gg/58HCd8NHuX"))

#Loot_gen knopf unter Erschwernes Entry
Loot_gen =tk.Button(lootf,   #verknüpfung zum hauptfenster
                   text= knopf_text,
                   command=DSALoot,
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
             padx=3,
             pady=3)

#Erschwernis Entry über Loot_gen knopf
erschwernisb = tk.Entry(lootf,   #verknüpfung zum hauptfenster
                        width=7,)
erschwernisb.configure()
erschwernisb.insert(0, "Erschw.")
erschwernisb.pack(side="bottom")

####################################################################
#Random encounter

encounterf = tk.Frame(root)
encounterf.config(bg=backgroud)
encounterf.pack(expand=1)
tabs.add(encounterf, text="Begegnungen")

#Überschrift
Fenster_überschrift = tk.Label(encounterf,    #verknüpfung zum hauptfenster
                  text= "Lass die Würfel Rollen",   #überschirft Fenstertext
                  font=(überschrift),   #Texteinstellungen über "überschrift"
                  bd=4,                 #Rand Dicke
                  relief="ridge")       #Rand art
Fenster_überschrift.configure(bg=backgroud) 
Fenster_überschrift.pack( fill="both",
            side="top",
            ipadx=10,
            ipady=5)

#Combobox
select_ort = tk.StringVar()
ort_cb = ttk.Combobox(encounterf, textvariable=select_ort)
ort_cb['values']  = el.namen_main
ort_cb['state'] = 'readonly'
ort_cb.current(0)
ort_cb.pack()

#Item Label unter überschrift
Ort_über = tk.Label(encounterf,      #verknüpfung zum hauptfenster
                 font=(überschrift))
Ort_über.configure(bg=backgroud)
Ort_über.pack(ipady=5)

#
Ort_begeg_n = tk.Label(encounterf,      #verknüpfung zum hauptfenster
                 font=(subüberschrift))
Ort_begeg_n.configure(bg=backgroud)
Ort_begeg_n.pack(ipady=5)


#
Ort_begeg = tk.Label(encounterf,      #verknüpfung zum hauptfenster
                 font=(schrift),
                 wraplength=300,
                 height=4)
Ort_begeg.configure(bg=backgroud)
Ort_begeg.pack(ipady=50)

#Support Label unter Loot_gen knopf
Support = tk.Label(encounterf,    #verknüpfung zum hauptfenster
                  text="Discord für Support und Ideen",
                  font=(subschrift),
                  cursor="hand2")
Support.configure(bg=backgroud)
Support.pack( fill="y",
            side="bottom",
            ipadx=3,
            ipady=5)
Support.bind("<Button-1>", lambda e: ll.callback("https://discord.gg/58HCd8NHuX"))

#enc_gen knopf unter Erschwernes Entry
enc_gen =tk.Button(encounterf,   #verknüpfung zum hauptfenster
                   text= "Das Geschehen",
                   command= lambda: Ereignis(),
                   font=(knopfschrift),
                   
                   width=120,
                   bd=7,
                   relief="groove")
enc_gen.configure(bg=backgroud,
                  activebackground=button_press,
                  height=20,
                  )
enc_gen.pack(side="bottom",
             ipadx=0,
             ipady=0,
             padx=0,
             pady=1)

root.mainloop()