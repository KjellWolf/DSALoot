#!/usr/bin/python3

#Schneider Gabriel / 23-08-2022
#Encounter Listen

from random import randint
import encounterlistestadt as els
import encounterlistelandst as ell
import encounterlistedorf as eld
import encounterlistewald as elw
import encounterlistesonst as elso
####################################################################
#dropdown Liste für Region auswahl
namen_main = ["In der Stadt",                       #Liste Fertig
              "Auf der Landstraße",
              "Im Dorf",
              "In der Wildnis",
              "Übernachtunsgplatz",
              "In der Taverne"]

####################################################################
#Listen Längen Berechnen
#stadt
stadt_c         = len(els.stadt_main)       -1

#landstraße
landste_c       = len(ell.landst_main)      -1

#Dorf
dorf_c          = len(eld.dorf_main)        -1

#Wald   
wald_c          = len(elw.wald_main)        -1

#Wald übernachtunsgplatz
über_so_c        = len(elso.wald_über)      -1

#Taverne
tavern_so_c      = len(elso.in_tavern)      -1

####################################################################

def Stadt():
    #Überschrift
    ran = randint(0,stadt_c)
    name = els.stadt_main[ran] 
    
    #Zufallsbegegnung   
    text = els.stadt_liste[ran]
    text_c = len(text) -1
    text_ran = randint(0,text_c)
    begeg = text[text_ran]
    
    print(name)
    print(begeg)
    return(name, begeg)   
      
def Landstr():
    #Überschrift
    ran = randint(0,landste_c)
    name = ell.landst_main[ran] 
    
    #Zufallsbegegnung   
    text = ell.landst_liste[ran]
    text_c = len(text) -1
    text_ran = randint(0,text_c)
    begeg = text[text_ran]
    
    print(name)
    print(begeg)
    return(name, begeg)  

def Dorf():      
    #Überschrift
    ran = randint(0,stadt_c)
    name = eld.dorf_main[ran] 
    
    #Zufallsbegegnung   
    text = eld.dorf_liste[ran]
    text_c = len(text) -1
    text_ran = randint(0,text_c)
    begeg = text[text_ran]
    
    print(name)
    print(begeg)
    return(name, begeg)  

def Wald():
    #Überschrift
    ran = randint(0,wald_c)
    name = elw.wald_main[ran] 
    
    #Zufallsbegegnung   
    text = elw.wald_liste[ran]
    text_c = len(text) -1
    text_ran = randint(0,text_c)
    begeg = text[text_ran]
    
    print(name)
    print(begeg)
    return(name, begeg)  

def üNachtW():
        #Überschrift
    ran = randint(0,über_so_c)
    name = elso.wald_über[ran] 
    
    begeg = None
    print(name)
    return(begeg, name)

def inTavern():
        #Überschrift
    ran = randint(0,tavern_so_c)
    name = elso.in_tavern[ran] 
    
    begeg = None
    print(name)
    return(begeg, name)

