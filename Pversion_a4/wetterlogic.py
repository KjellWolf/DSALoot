#!/usr/bin/python3

#Schneider Gabriel / 23-08-2022
#Encounter Listen


from random import randint

####################################################################
#Liste JZeit
JZeit =["Frühling",
        "Sommer",
        "Herbst",
        "Winter",
        "Regenzeit",
        "Trockenzeit"]

####################################################################
#Liste Biom
Biom = ["Ewiges Eis",
            "Tundra / Subpolare Klimazone",
            "Taiga / Gemäßigt Kaltes Klima",
            "Gemäßigtes Klima",
            "Subtropisches Klima",
            "Wüste",
            "Tropen"] 

####################################################################
#Liste WindMain
WindMain = ["Windstill",
            "Windstill",
            "Windstill",
            "Laues Lüftchen",
            "Leichte Brise",
            "Frische Brise",
            "Steife Brise",
            "Sturm",
            "Starker Sturm",
            "Starker Sturm",
            "Orkan"]

####################################################################
#Liste TempMain
TempMain = ["Sehr Kalt",
            "Kalt",
            "Kühl",
            "Kühl",
            "Normal",
            "Normal",
            "Warm",
            "Warm", 
            "Sehr Warm",
            "Heiß",
            "Sehr Heiß",
            "Sehr Heiß"]

####################################################################

####################################################################



def WindTemp():
    global rWind
    global rTemp
    rWind = randint(0,5)

    rTemp = randint(0,5)
    
####################################################################
def EEis():
    
    WindTemp()
    
    global Main
    
    Main = randint(1,20)

    global wett
    global temp
    global wind
      
    if Main <= 4: 
        wett = "Klar"
        
        windz = rWind + 2
        wind = WindMain[windz]
        
        tempz =rTemp + 0
        temp = TempMain[tempz]   
        
    if Main >= 5 and Main <= 12: 
        wett = "Bedeckt"
        
        windz = rWind + 1
        wind = WindMain[windz]
        
        tempz =rTemp + 1
        temp = TempMain[tempz]

    if Main >= 13 and Main <= 15: 
        wett = "Bedeckt, Leichter Schneefall"
        
        windz = rWind + 2
        wind = WindMain[windz]
        
        tempz =rTemp + 1
        temp = TempMain[tempz]

    if Main >= 16 and Main <= 18: 
        wett = "Bedeckt, stetiger Schneefall"
        
        windz = rWind + 3
        wind = WindMain[windz]
        
        tempz =rTemp + 1
        temp = TempMain[tempz]

    if Main >= 19 and Main <= 20: 
        wett = "Heftiger Schneefall"
        
        windz = rWind + 5
        wind = WindMain[windz]
        
        tempz =rTemp + 0
        temp = TempMain[tempz]

def Tundra():
    
    WindTemp()
    
    global Main
    
    Main = randint(1,20)
    
    global wett
    global temp
    global wind
    
    
    if Main <= 6: 
        wett = "Klar"
        
        windz = rWind + 2
        wind = WindMain[windz]
        
        tempz =rTemp + 0
        temp = TempMain[tempz]   
        
    if Main >= 7 and Main <= 12: 
        wett = "Bedeckt"
        
        windz = rWind + 1
        wind = WindMain[windz]
        
        tempz =rTemp + 1
        temp = TempMain[tempz]

    if Main >= 13 and Main <= 16: 
        wett = "Bedeckt, Leichter Niederschlag"
        
        windz = rWind + 2
        wind = WindMain[windz]
        
        tempz =rTemp + 1
        temp = TempMain[tempz]

    if Main >= 17 and Main <= 19: 
        wett = "Bedeckt, stetiger Niederschlag"
        
        windz = rWind + 3
        wind = WindMain[windz]
        
        tempz =rTemp + 1
        temp = TempMain[tempz]

    if Main >= 20: 
        wett = "Stürmisch"
        
        windz = rWind + 5
        wind = WindMain[windz]
        
        tempz =rTemp + 0
        temp = TempMain[tempz]

def TaigaSomm():
    
    WindTemp()
    
    global Main
    
    Main = randint(1,20)
    
    global wett
    global temp
    global wind
    
    
    if Main <= 8: 
        wett = "Klar"
        
        windz = rWind + 2
        wind = WindMain[windz]
        
        tempz =rTemp + 3
        temp = TempMain[tempz]   
        
    if Main >= 9 and Main <= 10: 
        wett = "Bedeckt"
        
        windz = rWind + 1
        wind = WindMain[windz]
        
        tempz =rTemp + 2
        temp = TempMain[tempz]

    if Main >= 11 and Main <= 13: 
        wett = "Bedeckt, Leichter Niederschlag"
        
        windz = rWind + 2
        wind = WindMain[windz]
        
        tempz =rTemp + 1
        temp = TempMain[tempz]

    if Main >= 14 and Main <= 15: 
        wett = "Bedeckt, starker Niederschlag"
        
        windz = rWind + 3
        wind = WindMain[windz]
        
        tempz =rTemp + 0
        temp = TempMain[tempz]

    if Main >= 16: 
        wett = "Starker Dauerregen"
        
        windz = rWind + 5
        wind = WindMain[windz]
        
        tempz =rTemp + 0
        temp = TempMain[tempz]
    
def TaigaSonst():    
    
    WindTemp()
    
    global Main
    
    Main = randint(1,20)
    
    global wett
    global temp
    global wind
    
    
    if Main <= 6: 
        wett = "Klar"
        
        windz = rWind + 2
        wind = WindMain[windz]
        
        tempz =rTemp + 3
        temp = TempMain[tempz]   
        
    if Main >= 7 and Main <= 12: 
        wett = "Bedeckt"
        
        windz = rWind + 1
        wind = WindMain[windz]
        
        tempz =rTemp + 2
        temp = TempMain[tempz]

    if Main >= 13 and Main <= 15: 
        wett = "Bedeckt, Leichter Niederschlag"
        
        windz = rWind + 2
        wind = WindMain[windz]
        
        tempz =rTemp + 1
        temp = TempMain[tempz]

    if Main >= 16 and Main <= 18: 
        wett = "Bedeckt, starkr Niederschlag"
        
        windz = rWind + 3
        wind = WindMain[windz]
        
        tempz =rTemp + 0
        temp = TempMain[tempz]

    if Main >= 19: 
        wett = "Staker Dauerregen"
        
        windz = rWind + 5
        wind = WindMain[windz]
        
        tempz =rTemp + 0
        temp = TempMain[tempz]
        
def GemäßSomm():
    
    WindTemp()
    
    global Main
    
    Main = randint(1,20)
    
    global wett
    global temp
    global wind
    
    
    if Main <= 7: 
        wett = "Klar"
        
        windz = rWind + 2
        wind = WindMain[windz]
        
        tempz =rTemp + 4
        temp = TempMain[tempz]   
        
    if Main >= 8 and Main <= 12: 
        wett = "Bedeckt"
        
        windz = rWind + 1
        wind = WindMain[windz]
        
        tempz =rTemp + 3
        temp = TempMain[tempz]

    if Main >= 13 and Main <= 15: 
        wett = "Bedeckt, Leichter Niederschlag"
        
        windz = rWind + 2
        wind = WindMain[windz]
        
        tempz =rTemp + 2
        temp = TempMain[tempz]

    if Main >= 16 and Main <= 18: 
        wett = "Bedeckt, starker Niederschlag"
        
        windz = rWind + 3
        wind = WindMain[windz]
        
        tempz =rTemp + 0
        temp = TempMain[tempz]

    if Main >= 19: 
        wett = "Wolkenbruch"
        
        windz = rWind + 5
        wind = WindMain[windz]
        
        tempz =rTemp + 1
        temp = TempMain[tempz]
    
def GemäßHeFr():
        
    WindTemp()
    
    global Main
    
    Main = randint(1,20)
    
    global wett
    global temp
    global wind
    
    
    if Main <= 6: 
        wett = "Klar"
        
        windz = rWind + 2
        wind = WindMain[windz]
        
        tempz =rTemp + 4
        temp = TempMain[tempz]   
        
    if Main >= 7 and Main <= 8: 
        wett = "Bedeckt"
        
        windz = rWind + 1
        wind = WindMain[windz]
    
        tempz =rTemp + 3
        temp = TempMain[tempz]

    if Main >= 9 and Main <= 10: 
        wett = "Nebelig"
        
        windz = rWind + 0
        wind = WindMain[windz]
        
        tempz =rTemp + 1
        temp = TempMain[tempz]

    if Main >= 11 and Main <= 14: 
        wett = "Bedeckt, Leichter Niederschlag"
        
        windz = rWind + 2
        wind = WindMain[windz]
        
        tempz =rTemp + 2
        temp = TempMain[tempz]

    if Main >= 15 and Main <= 17: 
        wett = "Bedeckt, starker Niederschlag"
        
        windz = rWind + 3
        wind = WindMain[windz]
        
        tempz =rTemp + 2
        temp = TempMain[tempz]

    if Main >= 18: 
        wett = "Wolkenbruch"
        
        windz = rWind + 5
        wind = WindMain[windz]
        
        tempz =rTemp + 1
        temp = TempMain[tempz]
        
def Subtrotro():
    
    WindTemp()
    
    global Main
    
    Main = randint(1,20)
    
    global wett
    global temp
    global wind
    
    
    if Main <= 6: 
        wett = "Klar"
        
        windz = rWind + 1
        wind = WindMain[windz]
        
        tempz =rTemp + 6
        temp = TempMain[tempz]   
        
    if Main == 7: 
        wett = "Schwül, Dünstig"
        
        windz = rWind + 0
        wind = WindMain[windz]
        
        tempz =rTemp + 6
        temp = TempMain[tempz]

    if Main >= 8 and Main <= 12: 
        wett = "Bedeckt"
        
        windz = rWind + 1
        wind = WindMain[windz]
        
        tempz =rTemp + 1
        temp = TempMain[tempz]

    if Main >= 13 and Main <= 16: 
        wett = "Bedeckt, Leichter Niederschlag"
        
        windz = rWind + 2
        wind = WindMain[windz]
        
        tempz =rTemp + 3
        temp = TempMain[tempz]
        
    if Main >= 17 and Main <= 19: 
        wett = "Bedeckt, starker Niederschlag"
        
        windz = rWind + 3
        wind = WindMain[windz]
        
        tempz =rTemp + 2
        temp = TempMain[tempz]

    if Main >= 20: 
        wett = "Starker Dauerregen"
        
        windz = rWind + 5
        wind = WindMain[windz]
        
        tempz =rTemp + 2
        temp = TempMain[tempz]
    
def Subtroreg():    
    
    WindTemp()
    
    global Main
    
    Main = randint(1,20)
    
    global wett
    global temp
    global wind
    
    
    if Main <= 2: 
        wett = "Klar"
        
        windz = rWind + 1
        wind = WindMain[windz]
        
        tempz =rTemp + 6
        temp = TempMain[tempz]   
        
    if Main >= 3 and Main <= 7: 
        wett = "Schwül, Dünstig"
        
        windz = rWind + 0
        wind = WindMain[windz]
        
        tempz =rTemp + 6
        temp = TempMain[tempz]

    if Main >= 8 and Main <= 11: 
        wett = "Bedeckt, Leichter Niederschlag"
        
        windz = rWind + 2
        wind = WindMain[windz]
        
        tempz =rTemp + 3
        temp = TempMain[tempz]

    if Main >= 12 and Main <= 17: 
        wett = "Bedeckt, starker Niederschlag"
        
        windz = rWind + 3
        wind = WindMain[windz]
        
        tempz =rTemp + 2
        temp = TempMain[tempz]

    if Main >= 18: 
        wett = "Starker Dauerregen"
        
        windz = rWind + 5
        wind = WindMain[windz]
        
        tempz =rTemp + 2
        temp = TempMain[tempz]
    
def Wüste():
    
    WindTemp()
    
    global Main
    
    Main = randint(1,20)
    
    global wett
    global temp
    global wind
    
    
    if Main <= 16: 
        wett = "Klar"
        
        windz = rWind + 0
        wind = WindMain[windz]
        
        tempz =rTemp + 6
        temp = TempMain[tempz]   
        
    if Main >= 17 and Main <= 18: 
        wett = "einzelnde Wolken"
        
        windz = rWind + 1
        wind = WindMain[windz]
        
        tempz =rTemp + 4
        temp = TempMain[tempz]

    if Main == 19: 
        wett = "Bedeckt"
        
        windz = rWind + 2
        wind = WindMain[windz]
        
        tempz =rTemp + 3
        temp = TempMain[tempz]

    if Main == 20: 
        wett = "Bedeckt, Starker Niederschlag"
        
        windz = rWind + 5
        wind = WindMain[windz]
        
        tempz =rTemp + 2
        temp = TempMain[tempz]

def Tropentro():
    
    WindTemp()
    
    global Main
    
    Main = randint(1,20)
    
    global wett
    global temp
    global wind
    
    
    if Main <= 4: 
        wett = "Klar"
        
        windz = rWind + 1
        wind = WindMain[windz]
        
        tempz =rTemp + 5
        temp = TempMain[tempz]   
        
    if Main >= 5 and Main <= 15: 
        wett = "Schwül, Dünstig"
        
        windz = rWind + 0
        wind = WindMain[windz]
        
        tempz =rTemp + 5
        temp = TempMain[tempz]

    if Main >= 16 and Main <= 19: 
        wett = "Bedeckt"
        
        windz = rWind + 2
        wind = WindMain[windz]
        
        tempz =rTemp + 1
        temp = TempMain[tempz]

    if Main == 20: 
        wett = "Bedeckt, Starker Niederschlag"
        
        windz = rWind + 5
        wind = WindMain[windz]
        
        tempz =rTemp + 1
        temp = TempMain[tempz]
        
def Tropenreg():
    
    WindTemp()
    
    global Main
    
    Main = randint(1,20)
    
    global wett
    global temp
    global wind
    
    
    if Main <= 2: 
        wett = "Klar"
        
        windz = rWind + 1
        wind = WindMain[windz]
        
        tempz =rTemp + 5
        temp = TempMain[tempz]   
        
    if Main >= 3 and Main <= 6: 
        wett = "Schwül, Dünstig"
        
        windz = rWind + 0
        wind = WindMain[windz]
        
        tempz =rTemp + 15
        temp = TempMain[tempz]

    if Main >= 7 and Main <= 8: 
        wett = "Bedeckt"
        
        windz = rWind + 2
        wind = WindMain[windz]
        
        tempz =rTemp + 3
        temp = TempMain[tempz]

    if Main >= 9 and Main <= 14: 
        wett = "Bedeckt, leichter Niederschlag"
        
        windz = rWind + 2
        wind = WindMain[windz]
        
        tempz =rTemp + 4
        temp = TempMain[tempz]

    if Main >= 15: 
        wett = "Bedeckt, Starker Niederschlag"
        
        windz = rWind + 5
        wind = WindMain[windz]
        
        tempz =rTemp + 1
        temp = TempMain[tempz]