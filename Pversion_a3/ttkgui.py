#!/usr/bin/python3

#Schneider Gabriel / 15-08-2022
#Zufall für Loot

from random import randint
from tkinter import BOTH, CENTER, E, N, S, W, StringVar, ttk
import tkinter as tk


import lootlogic as ll 
import encounterlogic as el



#funktion Loot
def Loot():
        #Item
        erschwernis = 0
        erschwernis = erschw.get()
        item = ll.Loot_main(erschwernis)
        mods = ll.Mod(item)
        
        #reset
        mod1N.set('')
        mod2N.set('')
        mod3N.set('')
        mod4N.set('')
        
        #set
        itemN.set(item)
        try:
            mod1N.set(mods[0])
        except IndexError:
            pass
        try:
            mod2N.set(mods[1])
        except IndexError:
            pass
        try:
            mod3N.set(mods[2])
        except IndexError:
            pass
        try:
            mod4N.set(mods[3])
        except IndexError:
            pass
        
        
'''
def Ereignis():
    ort = select_ort.get()
    Ort_über.config(text=ort)
    
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
    
    Ort_begeg_n.config(text=begegnung[0])
    Ort_begeg.config(text=begegnung[1])
'''
   
    
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
fbackgroud = "#719DB0"
fbutton_press = "#61808D"

####################################################################
#Fenster aufbau und aussehen

root = tk.Tk()              #Hauptfenster Bestimmen
root.title(titel_text)      #Fenster Titel Setzen über "titel_text"
#root.iconbitmap('Python\Loot\Pversion_a3\Dateien\Fox.ico')  #Fenster Icon setzen
root.geometry("420x500")    #Fenster Startgröße setzen in pixel
root.config(bg=fbackgroud)   #Fenster hintergund setzen über "background"
root.columnconfigure(0, weight=1)         # numbering beginns with 0 for old Tk widgets
root.rowconfigure(0, weight=1) 
root.resizable(False, False) 
#Tabs oberste Leiste
tabs = ttk.Notebook(root)
tabs.grid(row=0, sticky=(W,N,E,S))

#Frame Loot
lootF = ttk.Frame(root, borderwidth=2, relief='sunken', \
                        width=418, height=500, padding='80 20 80 20')
lootF.propagate(0)
lootF.grid(row=2, sticky=(W, N, E, S))
tabs.add(lootF, text="Loot")


#Ausgabe
itemF = ttk.Frame(lootF, height=400)
itemF.pack(side="top")

#Item Name
itemN = StringVar()
itemL = ttk.Label(itemF, textvariable=itemN, compound=CENTER)
itemL.grid(row=1, column=2, sticky=N)
    #Mod1
mod1N = StringVar()
mod1 = ttk.Label(itemF, textvariable=mod1N, compound=CENTER)
mod1.grid(row=2, column=2, sticky=N)
    #Mod2
mod2N = StringVar()
mod2 = ttk.Label(itemF, textvariable=mod2N, compound=CENTER)
mod2.grid(row=3, column=2, sticky=N)
    #Mod3
mod3N = StringVar()
mod3 = ttk.Label(itemF, textvariable=mod3N, compound=CENTER)
mod3.grid(row=4, column=2, sticky=N)
    #Mod4
mod4N = StringVar()
mod4 = ttk.Label(itemF, textvariable=mod4N, compound=CENTER)
mod4.grid(row=5, column=2, sticky=(N, S))


#Eingabe Frame
eingF = ttk.Frame(lootF, width=450)
eingF.pack(side="bottom")

#Entry Erschw.
erschwN = ttk.Label(eingF, text="      Erschw:")
erschwN.grid(row=1, column=1, sticky=(W, E), columnspan=3)
erschw = StringVar()
erschwE = ttk.Entry(eingF, textvariable=erschw, width=6)
erschwE.grid(row=1, column=2, sticky=(S))

#Button Loot
lootB = ttk.Button(eingF, text=knopf_text, command=Loot, width=40,)
lootB.grid(row=2,column=2, sticky=(W, E), columnspan=1, ipady=20)


#Support Discord
Support = tk.Label(eingF, text="Discord für Support und Ideen", font=(subschrift), cursor="hand2")
Support.grid(row=3, columnspan=3)
Support.bind("<Button-1>", lambda e: ll.callback("https://discord.gg/58HCd8NHuX"))


#Frame Encounter
encF = ttk.Frame(root, borderwidth=2, relief='sunken', \
                        width=418, height=500, padding='80 20 80 20')
encF.propagate(0)
encF.grid(row=2, sticky=(W, N, E, S))
tabs.add(encF, text="Encounter")


textF = ttk.Frame(encF, height=400)
textF.pack(side="top")

#Auswahl des Ortes
select_ort = tk.StringVar()
ort_cb = ttk.Combobox(textF, textvariable=select_ort)
ort_cb['values']  = el.namen_main
ort_cb['state'] = 'readonly'
ort_cb.current(0)
ort_cb.grid(row=0, column=2)

#Situations Überschrift
OrtN = StringVar()
OrtL = ttk.Label(textF, textvariable=itemN, compound=CENTER)
OrtL.grid(row=1, column=2, sticky=N)

#Begegnungstext
begegN = StringVar()
begegL = ttk.Label(textF, textvariable=mod1N, compound=CENTER)
begegL.grid(row=2, column=2, sticky=N)

################################################################
#Encounter Eingabe
eeinF = ttk.Frame(encF, width=450)
eeinF.pack(side="bottom")

#Zufalls button
encB = ttk.Button(eeinF, text='Das Geschehen', command=Loot, width=40,)
encB.grid(row=1,column=2, sticky=(W, E), columnspan=1, ipady=20)

#Support Discord
Support = tk.Label(eeinF, text="Discord für Support und Ideen", font=(subschrift), cursor="hand2")
Support.grid(row=3, columnspan=3)
Support.bind("<Button-1>", lambda e: ll.callback("https://discord.gg/58HCd8NHuX"))

root.mainloop()