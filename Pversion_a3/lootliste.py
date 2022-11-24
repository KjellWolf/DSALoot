#!/usr/bin/python3

#Schneider Gabriel / 15-08-2022
#Listen für Main.py



schrott = ["Fussel",             
        "Flusen",                        
        "Verrossteter Schlüssel",
        "Alter Liebesbrief",
        "Holzmurmeln",                   
        "Fünf Eicheln",
        "Socke",                    
        "Bittschrift eines Schuldners", 
        "Eine Ordentliche Prise Salz",
        "Zettel mit Wirren Zahlen",      
        "Angefangener Liebesbrief",     
        "Kinderzeichnug eines Baums",
        "Büchel Haare",                  
        "Getrokneter Kot im Beutel",     
        "Sehr Beißender schnupftaback",  
        "Gebrauchtes Taschentuch",       
        "Unleserliches Notzizbuch",      
        "Einkaufliste",                  
        "Hand Voll Asche",
        "Halbfertige Wachsfigur",
        "Finger",
        "Nichts"]

normal = ["Wollknäul",           
        "Billiger Kautabak",             
        "Stück Kreide",                  
        "Tintenfass",                   
        "Ruß zum Schminken",             
        "Strohhut",
        "Nägel",                         
        "Kiste voller Fischschuppen",    
        "Dicke Wurzel",                  
        "Kleine Schnapsflasche",         
        "Tierknochen",                   
        "Trokene Brotkante",
        "Zähne im Lederbeutel",          
        "Pfeife mit Tabak",              
        "Siegelwachs",                   
        "Buntes Haarband",               
        "Tote Maus",
        "Teil einer Schatzkarte",        
        "Tinkturen",                     
        "Tontigel mit Fettsalbe",
        "Schreibfeder"]         


selten = ["Götterstatuette",     
        "Gesichtspuder",                 
        "Ring mit Göttersymbol",         
        "Räucherstäbchen",               
        "Ausgestopfte Krähe",           
        "Halskette in Tierform",         
        "Bauskizzen eines Anwesen",      
        "Gewürz",                        
        "Talisman aus Federn",                    
        "Schleier",                      
        "Schlangenhaut",                 
        "Kartenset für Wahrsagerrei",    
        "Figurtiere der 12 Götter",
        "Miniatur eines Hirsches",
        "Flöte",                         
        "Einfacher Holzring",            
        "Exquisiter schnaps",            
        "Premer feuer 1 Schank",         
        "Fuchspelz",                     
        "Bronzener Armreif"]              
 

sehr_selten = ["Getrocknete Teeblätter",  
                "Ilmenblatt",                    
                "Münzsack",                                  
                "Kaputter Kompass",
                "Stirnreif",                     
                "Granatkristall",                
                "Smaragtgrüne Schreibtinte",     
                "Aquamarin",                     
                "Faustgroßer Würfel",
                "Faltmesser",                       
                "12 Göttliches Gebetsbuch",      
                "Bronzekrone",                        
                "Eigen magnetischer Erzklumpen", 
                "Augenimitat aus Elfenbein",
                "Wolfsfell Waldwolf",            
                "Kristallpokal",
                "Bronzeschatulle mit Tabak",      
                "Weißes Wolfsfell",              
                "Phiole mit verschluss",         
                "Klingende Spieluhr"]

epic = ["Edelstein",             
        "Mondsilberklumpen",              
        "Goldenes Zepter",              
        "Perlenkette",                   
        "Silberbesteck",                 
        "Kurzstab mit Rabenkopf",
        "Silberkette mit Juwel",
        "verziertes Fernrohr",
        "Gemälde einer Alten Tulamidin",     
        "Besitzuhrkunde für länderreien",    
        "Einfache Krone",                   
        "Edler Dolch aus Silber",           
        "Wertscheine der Nordlandbank",   
        "Vinsalter Ei",                     
        "Emblem des Herscherhauses",     
        "Alt Bosbaranische Vase",            
        "Brokatrobe",                     
        "Kerzenleuchter",
        "Elfenkurzbogen aus Elfenbein",   
        "Roter Goldfälser Wein 1 Schank"]



####################################################################
quali = ["Alter Liebesbrief",
        "Teil einer Schatzkarte", 
        "Halskette in Tierform",
        "Schlangenhaut",
        "Flöte",
        "Fuchspelz",
        "Bronzener Armreif", 
        "Getrocknete Teeblätter",
        "Münzsack",
        "Faltmesser",
        "Bronzekrone",
        "Wolfsfell Waldwolf",
        "Bronzeschatulle mit Tabak",
        "Weißes Wolfsfell",
        "Edelstein",
        "Perlenkette", 
        "Silberbesteck",
        "Gemälde einer Alten Tulamidin",
        "Strohhut",
        "Schreibfeder",
        "Alt Bosbaranische Vase",
        "Schleier",
        "Elfenkurzbogen aus Elfenbein",
        "Vinsalter Ei",
        "Gewürz"]

farbe = ["Fussel",
        "Flusen",
        "Socke",
        "Büchel Haare",
        "Gebrauchtes Taschentuch",
        "Unleserliches Notzizbuch",
        "Wollknäul",
        "Stück Kreide",
        "Buntes Haarband",
        "Tinkturen",
        "Schleier",
        "Stirnreif",
        "Edelstein",
        "Alt Bosbaranische Vase",
        "Siegelwachs",
        "Gewürz"]

anzahl = ["Holzmurmeln",
        "Einkaufliste",
        "Wollknäul",
        "Stück Kreide",
        "Nägel",
        "Tierknochen",
        "Zähne im Lederbeutel",
        "Buntes Haarband",
        "Räucherstäbchen",
        "Talisman aus Federn",
        "Einfacher Holzring",
        "Granatkristall",
        "Aquamarin",
        "Schreibfeder"]

portionen = ["Sehr Beißender schnupftaback",
            "Billiger Kautabak",
            "Ruß zum Schminken",
            "Pfeife mit Tabak", 
            "Siegelwachs", 
            "Tontigel mit Fettsalbe",
            "Gesichtspuder",
            "Gewürz",
            "Getrocknete Teeblätter",
            "Ilmenblatt",
            "Smaragtgrüne Schreibtinte",
            "Bronzeschatulle mit Tabak",]

füllstand = ["Tintenfass",
            "Kleine Schnapsflasche",
            "Exquisiter schnaps",
            "Phiole mit verschluss"]

seite = ["Socke"]

metall_zusatz = ["Nägel",
                 "Faltmesser",
                 "Vinsalter Ei"]

gott = ["Götterstatuette",
        "Ring mit Göttersymbol",
        "12 Göttliches Gebetsbuch"]

gott_tier = ["Halskette in Tierform"]

verwesung = ["Finger",
             "Tote Maus",
             "Dicke Wurzel"]