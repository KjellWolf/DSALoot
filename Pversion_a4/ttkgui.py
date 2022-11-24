#!/usr/bin/python3

#Schneider Gabriel / 15-08-2022
#Zufall für Loot

from random import randint
from tkinter import BOTH, CENTER, E, N, S, W, StringVar, ttk, font
import tkinter as tk


import lootlogic as ll 
import encounterlogic as el
import wetterlogic as wl


####################################################################
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
        
def Ereignis():
    ort = select_ort.get()
#    Ort_über.config(text=ort)
    global begeg_n
    global begeg_t
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
    
    begeg_n = begegnung[0]
    begeg_t = begegnung[1]
    OrtN.set(begegnung[0])
    begegN.set(begegnung[1])
  
def JzCbUpdate(self):
    
    Biom = select_Biom.get() 
    
    if Biom == "Ewiges Eis" or Biom == "Tundra / Subpolare Klimazone":
        Jz = ("Winter")
                
    if Biom == "Taiga / Gemäßigt Kaltes Klima" or Biom == "Gemäßigtes Klima":
        Jz = ("Frühling", "Sommer", "Herbst", "Winter")
    
    if Biom == "Subtropisches Klima"or Biom == "Tropen":
        Jz = ("Regenzeit", "Trockenzeit")
        
    if Biom == "Wüste":
        Jz = ("Sommer")            
        
    jz_cb['values']  = Jz
    jz_cb.current(0)

def WetterLogic():
        
    Biom = select_Biom.get()
    Jahreszeit = select_jz.get()  
    zusatzN.set('')
    
    if Biom == "Ewiges Eis":
        wl.EEis()
              
    if Biom == "Tundra / Subpolare Klimazone":
        wl.Tundra()
        
    if Biom == "Taiga / Gemäßigt Kaltes Klima":
        if Jahreszeit == "Sommer":
            wl.TaigaSomm()    
        
        else:
            wl.TaigaSonst()      

    if Biom == "Gemäßigtes Klima":
        if Jahreszeit == "Sommer":
            wl.GemäßSomm()

        elif Jahreszeit == "Winter":
            wl.TaigaSonst()
        
        else:
            wl.GemäßHeFr
            
    if Biom == "Subtropisches Klima":
        if Jahreszeit == "Regenzeit":
            wl.Subtroreg()
            
        if Jahreszeit == "Trockenzeit":
            wl.Subtrotro()            

    if Biom == "Tropen":
        if Jahreszeit == "Regenzeit":
            wl.Tropenreg()
            
        if Jahreszeit == "Trockenzeit":
            wl.Tropentro()  
            
    if Biom == "Wüste":
        wl.Wüste()

            
    wetterN.set(wl.wett)
    tempN.set(wl.temp)
    windN.set(wl.wind)

tagez = 0                        
MainAnder = 0

def Wetter():
    global wetter
    global MainAnder
    global tagez
    
    tagez = tagez +1
    tage = str(tagez)
    tage = "{}. Tag".format(tagez)  
    tageN.set(tage)

    
    if MainAnder == 0: #Erstwurf
        WetterLogic()
        
        MainAnder = 1
    else:
        MainAnder = randint(1,6)

        if MainAnder <= 3:
            wetter = wl.wett
            
            zusatz = "Keine Änderung zum Vortag"
            zusatzN.set(zusatz)
        
        if MainAnder == 4:
            wetterold = wl.Main
            
            zusatzN.set('')
            
            roll1 = WetterLogic()
            roll1wett = wl.Main
            
            roll2 = WetterLogic()
            roll2wett = wl.Main
            
            diff1 = wetterold - roll1wett
            diff2 = wetterold - roll2wett
            
            if diff1 >= diff2: 
                roll2
            else:    
                roll1
                
        if MainAnder == 5:
            wetter = WetterLogic()
            
            zusatzN.set('')
            
        if MainAnder == 6:
            wetter = WetterLogic()
            
            zusatz = "Wetterumschwung! Für den gleichen Tag nochmal Würfeln"
            zusatzN.set(zusatz)            
  
####################################################################
#Bereich für zufälle

#Zufalls Fenster Titel und versionsnummer   
title = ["Loot für Phex!",
         "Looten und Leveln!",
         "Get this you Thief!",
         "Nimm oder Stirb"]
count_title = len(title) -1
zufall_titel = randint(0, count_title)
titel_text = "V_a.4 " + title[zufall_titel] 

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


####################################################################
#Fenster aufbau und aussehen

root = tk.Tk()              #Hauptfenster Bestimmen
root.title(titel_text)      #Fenster Titel Setzen über "titel_text"
#root.iconbitmap('Python\Loot\Pversion_a3\Dateien\Fox.ico')  #Fenster Icon setzen
root.geometry("420x500")    #Fenster Startgröße setzen in pixel
root.config()   #Fenster hintergund setzen über "background"
root.columnconfigure(0, weight=1)         # numbering beginns with 0 for old Tk widgets
root.rowconfigure(0, weight=1) 
root.resizable(False, False) 
####################################################################
#Fonts
uberschrift = font.Font(family='Helvetica',
                          name='uberschrift',
                          size=17,
                          weight= 'bold',
                          underline=1
                        )

ntext = font.Font(family='Helvetica',
                          name='ntext',
                          size= 15
                        )
nwtext = font.Font(family='Helvetica',
                          name='nwtext',
                          size= 12
                        )
####################################################################
#Style
root.tk.call("lappend", "auto_path", "awthemes-10.4.0")
root.tk.call("package", "require", "awdark")
style = ttk.Style(root)
current_theme = style.theme_use("awdark")

style.configure('my.TButton', font=('Helvetica',14))

####################################################################
#Tabs oberste Leiste
tabs = ttk.Notebook(root)
tabs.grid(row=0, sticky=(W,N,E,S))

#Frame Loot
def LootTab():
    global itemN
    global mod1N
    global mod2N
    global mod3N
    global mod4N
    global erschw
    
    lootF = ttk.Frame(root, borderwidth=2, relief='sunken', \
                            width=428, height=500, padding='80 10 80 10')
    lootF.propagate(0)
    lootF.grid(row=2, sticky=(W, N, E, S))
    tabs.add(lootF, text="Loot")

    #Ausgabe
    itemF = ttk.Frame(lootF, height=450)
    itemF.pack(side="top")

    #Item Name
    itemN = StringVar()
    itemL = ttk.Label(itemF, textvariable=itemN, compound=CENTER, font=uberschrift, wraplength=250 , justify=CENTER)
    itemL.grid(row=1, column=2, sticky=N, pady=10)
        #Mod1
    mod1N = StringVar()
    mod1 = ttk.Label(itemF, textvariable=mod1N, compound=CENTER, font=ntext)
    mod1.grid(row=2, column=2, sticky=N)
        #Mod2
    mod2N = StringVar()
    mod2 = ttk.Label(itemF, textvariable=mod2N, compound=CENTER, font=ntext)
    mod2.grid(row=3, column=2, sticky=N)
        #Mod3
    mod3N = StringVar()
    mod3 = ttk.Label(itemF, textvariable=mod3N, compound=CENTER, font=ntext)
    mod3.grid(row=4, column=2, sticky=N)
        #Mod4
    mod4N = StringVar()
    mod4 = ttk.Label(itemF, textvariable=mod4N, compound=CENTER, font=ntext)
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
    lootB = ttk.Button(eingF, text=knopf_text, command=Loot, width=15, style='my.TButton')
    lootB.grid(row=2,column=2, sticky=(W, E), columnspan=1, ipady=20, ipadx=20)

    #Support Discord
    Support = ttk.Label(eingF, text="Discord für Support und Ideen", font=(subschrift), cursor="hand2")
    Support.grid(row=3, columnspan=3)
    Support.bind("<Button-1>", lambda e: ll.callback("https://discord.gg/58HCd8NHuX"))

LootTab()
#Frame Encounter
def EncTab():
    global select_ort
    global OrtN
    global begegN
    
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
    OrtL = ttk.Label(textF, textvariable=OrtN, compound=CENTER, font=uberschrift , wraplength=250, justify=CENTER)
    OrtL.grid(row=1, column=2, sticky=N, pady= 10)

    #Begegnungstext
    begegN = StringVar()
    begegL = ttk.Label(textF, textvariable=begegN, compound=CENTER, wraplength=250, justify=CENTER, font=ntext)
    begegL.grid(row=2, column=2)

    ################################################################
    #Encounter Eingabe
    eeinF = ttk.Frame(encF, width=450)
    eeinF.pack(side="bottom")

    #Zufalls button
    encB = ttk.Button(eeinF, text='Das Geschehen', command=Ereignis, width=15, style='my.TButton')
    encB.grid(row=1,column=2, sticky=(W, E), columnspan=1, ipady=20)

    #Support Discord
    Support = ttk.Label(eeinF, text="Discord für Support und Ideen", font=(subschrift), cursor="hand2")
    Support.grid(row=3, columnspan=3)
    Support.bind("<Button-1>", lambda e: ll.callback("https://discord.gg/58HCd8NHuX"))

EncTab()

#Frame Wetter
def WettTab():
    global select_Biom
    global select_jz
    global wetterN
    global tempN
    global windN
    global zusatzN
    global tageN
    global jz_cb
        
    WettF = ttk.Frame(root, borderwidth=2, relief='sunken', \
                            width=418, height=500, padding='80 20 80 20')
    WettF.propagate(0)
    WettF.grid(row=2, sticky=(W, N, E, S))
    tabs.bind("<<NotebookTabChanged>>", JzCbUpdate)
    tabs.add(WettF, text="Wetter")
    

    
    WetttF = ttk.Frame(WettF, height=400)
    WetttF.pack(side="top")

    #Auswahl des Bioms
    select_Biom = tk.StringVar()
    biom_cb = ttk.Combobox(WetttF, textvariable=select_Biom)
    biom_cb['values']  = wl.Biom
    biom_cb['state'] = 'readonly'
    biom_cb.current(0)
    biom_cb.grid(row=0, column=2, pady= 10)
    biom_cb.bind("<<ComboboxSelected>>", JzCbUpdate)

    #Auswahl des Bioms
    select_jz = tk.StringVar()
    jz_cb = ttk.Combobox(WetttF, textvariable=select_jz)
    jz_cb['state'] = 'readonly'
    jz_cb.grid(row=1, column=2, pady= 10)

    #wettertext
    wetterN = StringVar()
    wetterL = ttk.Label(WetttF, textvariable=wetterN, compound=CENTER, wraplength=250, justify=CENTER, font=nwtext)
    wetterL.grid(row=2, column=2, pady= 10)

    tempN = StringVar()
    tempL = ttk.Label(WetttF, textvariable=tempN, compound=CENTER, wraplength=250, justify=CENTER, font=nwtext)
    tempL.grid(row=3, column=2, pady= 10)

    windN = StringVar()
    windL = ttk.Label(WetttF, textvariable=windN, compound=CENTER, wraplength=250, justify=CENTER, font=nwtext)
    windL.grid(row=4, column=2, pady= 10)
    
    zusatzN = StringVar()
    zusatzL = ttk.Label(WetttF, textvariable=zusatzN, compound=CENTER, wraplength=250, justify=CENTER, font=nwtext)
    zusatzL.grid(row=5, column=2, pady= 10)
    
    tageN = StringVar()
    tageL = ttk.Label(WetttF, textvariable=tageN, compound=CENTER, wraplength=250, justify=CENTER, font=nwtext)
    tageL.grid(row=6, column=2, pady= 10)
    ################################################################
    #wetter eingabe
    WeinF = ttk.Frame(WettF, width=450)
    WeinF.pack(side="bottom")

    #Zufalls button
    encB = ttk.Button(WeinF, text='Das Wetter', command=Wetter, width=15, style='my.TButton')
    encB.grid(row=1,column=2, sticky=(W, E), columnspan=1, ipady=20)

    #Support Discord
    Support = ttk.Label(WeinF, text="Discord für Support und Ideen", font=(subschrift), cursor="hand2")
    Support.grid(row=3, columnspan=3)
    Support.bind("<Button-1>", lambda e: ll.callback("https://discord.gg/58HCd8NHuX"))
    
WettTab()
    
root.mainloop()