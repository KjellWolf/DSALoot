#!/usr/bin/python3

#Schneider Gabriel / 23-08-2022
#Encounter Listen

dorf_main = ["Ein Fest",
             "Das Dorf ist in Trauer",
             "Reisende machen Rast",
             "Probleme",
             "Religiöses",
             "Das Dorf wird Angegriffen",
             "Plagen",
             "Glaube",
             "Herrschaft",
             "Nächtliches",
             "Besondere Dorfbewohner",
             "Besondere Bauwerke",
             "Interaktion mit den Dorfbewohnern",
             "Schlechtes Wetter",
             "Magisches",
             "Das Dorf ist verlassen",
             "Eigenartiges",
             "Situationen",
             "Zauberer",
             "Geweihte"
               ]

####################################################################

dorf_fest =[
            "Da ganze Dorf hat sich zu einer Hochzeit versammelt, die Helden werden eingeladen.",
            "Die Dorfälteste (oder eine ähnliche Respektsperson) feiert Tsatag.",
            "Ein Kind wurde gerade geboren.",
            "Ein Festtag zu Ehren eines Regionalheiligen wird abgehalten.",
            "Eine neue Scheune ist fertig gestellt worden, alle feiern ein Richtfest.",
            "Eine besondere Persönlichkeit (ein Adliger, hoher Geweihter, bekannter Held …) besucht das Dorf."
           ]

dorf_trauer =[
            "Ein geschätztes Gemeindemitglied ist verstorben.",
            "Einige Dorfbewohner sind durch Hunger, Krankheit, Fluch oder bei einem Überfall ums Leben gekommen.",
            "Eine Seuche hat viele Tiere dahin gerafft.",
            "Es werden mehrere Dorfbewohner vermisst.",
            "Es wurden schon lange keine Kinder mehr geboren.",
            "Ein Wahrsager hat dem Dorf eine schlimme Zukunft prophezeit."
             ]

dorf_rast = [
            "Eine fahrende Händlerin bietet auf dem Dorfplatz ihre Waren feil.",
            "Ein fahrender Quacksalber oder Barbier bietet seine Waren und Dienste an.",
            "Eine Botenreiterin macht im Dorf Rast und erkundigt sich nach dem Weg.",
            "Eine Gruppe Abenteurer ist in der Gaststätte abgestiegen und stellt den Einheimischen merkwürdige Fragen.",
            "Ein Trupp Söldnerinnen oder Soldaten macht hier Halt und verlangt, versorgt zu werden.",
            "Eine Gauklertruppe oder ein Barde unterhält das Publikum."
            ]

dorf_probleme = [
                "Eine Dorfbewohnerin ist schwer erkrankt oder verletzt."
                "Es herrscht Streit im Dorf, die Helden werden um Rat gefragt.",
                "Ein Haus oder eine Scheune brennt.",
                "Der Brunnen ist versiegt.",
                "Mehrere Tiere sind aus ihrem Stall ausgebrochen.",
                "Ein Sturm hat viele Häuser im Dorf beschädigt."
                ]

dorf_religion = [
                "Eine Gruppe Pilger macht im Ort Rast und bittet um Gaben.",
                "Eine reisende Priesterin spricht freundlich mit den Einwohnern.",
                "Ein Schrein wird erbaut.",
                "Ein Schrein wurde von Unbekannten verwüstet.",
                "Ein Prediger hetzt gegen Unglauben, Adel, Helden, Sünde …",
                "Es wird gerade ein Fest zu Ehren eines Gottes abgehalten."
                ]

dorf_angriff = [
                "Räuber oder marodierende Söldner fallen über die Bevölkerung her.",
                "Die Haustiere werden von wilden Tieren (zum Beispiel Wölfen) heimgesucht.",
                "Orks, Goblins oder Achaz (je nach Region) greifen an.",
                "Die Landwehr des Nachbaradligen greift an.",
                "Im Dorf selbst gibt es zwei Fraktionen, die gerade übereinander herfallen.",
                "Ein Geist/Dämon/Drache terrorisiert das Dorf."
               ]

dorf_plagen = [
                "Eine Hungersnot ist ausgebrochen.",
                "Der Bach ist über die Ufer getreten und hat Teile des Dorfs überflutet.",
                "Es herrscht Dürre.",
                "Kleinere Erdbeben erschüttern das Dorf.",
                "Zahllose Mäuse oder Ratten sind über die Vorräte des Dorfs hergefallen.",
                "Schädlinge drohen die Ernte zu vernichten."
              ]

dorf_glaube = [
                "Die Einwohner verehren eine regionale Gottheit voller Inbrunst.",
                "Die Einwohner hängen einer Religion an, die für die Region untypisch ist.",
                "Die Einwohner verehren den Namenlosen.",
                "Die Einwohner verehren Naturgötter (zum Beispiel Sumu oder Satuaria).",
                "Die Einwohner geißeln sich voller Eifer.",
                "Die Einwohner vermischen unterschiedliche Religionen."
              ]

dorf_herrschaft = [
                    "Die Dorfbevölkerung lehnt sich gegen den Adligen auf.",
                    "Ein Ortsfremder hat die Herrschaft an sich gerissen, möglicherweise ein Ork oder eine Goblin-Schamanin.",
                    "Eine Magierin ist die höchste Autorität im Dorf.",
                    "Im Dorf herrscht das Recht des Stärkeren.",
                    "Die Dorfgemeinschaft trifft wichtige Entscheidungen gemeinsam.",
                    "Das Dorf ist seinem Herrscher treu ergeben."
                  ]

dorf_nacht = [
                    "Ein Dorfbewohner schlafwandelt.",
                    "Tiere geben eigenartige Laute von sich (fauchende Katzen, dauerndes Hundegebell, bellende Igel, eine kalbende Kuh schreit unablässig …).",
                    "Mitten in der Nacht reitet jemand im vollen Galopp durch das Dorf.",
                    "Betrunkene wanken laut von der Schenke nach Hause.",
                    "Ein Säugling schreit die ganze Nacht durch.",
                    "Jemand versucht die schlafenden Helden zu bestehlen."
                   ]

dorf_bdorfbewohner = [
                    "Eine bucklige Krüppelin brabbelt Eigenartiges vor sich hin.",
                    "Ein Albino gilt als Unglücksbringer.",
                    "Eine jugendliche Magiedilettantin hat ihre Kräfte überhaupt nicht unter Kontrolle.",
                    "Kriegsveteranen erzählen von ihren tollen Leistungen.",
                    "Eine Bewohnerin zeigt erstaunliche Ähnlichkeit mit einer berühmten Persönlichkeit oder einer Schwerverbrecherin.",
                    "Niemand weiß etwas über die Vergangenheit des schweigsamen Mannes, der sich hier vor einigen Jahren angesiedelt hat."
                     ]

dorf_bbauwerke = [
                "Ein erstaunlich großer Tempel steht am Dorfplatz.",
                "Die Schmiedin fertigt außerordentlich gute Waffen –verwunderlich für ein so einsames Dorf.",
                "Es gibt ein Badehaus.",
                "Der Dorfälteste hütet eine eigene Bibliothek.",
                "Eine Statue auf dem Dorfplatz erinnert an eine Heldin aus diesem Dorf oder ein besonderes Ereignis.",
                "Die Ruine einer großen Festung thront über dem Dorf."
                 ]

dorf_interak = [
                "Jemand aus dem Dorf will sich unbedingt den Helden anschließen.",
                "Die Dorfbewohner sind Fremden gegenüber besonders misstrauisch.",
                "Die Kinder spielen den Helden Streiche.",
                "Die Kinder wollen unbedingt von den Großtaten der Helden hören.",
                "Ein Dorfbewohner verliebt sich in einen der Helden.",
                "Die Dorfbewohner erwarten von den Helden ein Opfer für ihren Regionalgott."
               ]

dorf_wetter = [
                "Ein Hagelsturm zieht über das Land.",
                "Bei einem Gewitter schlägt der Blitz in die Dorflinde oder ein Gebäude ein.",
                "Hochwasser zerstört die Brücke / die Mühle.",
                "Ein Wirbelsturm zerstört mehrere Gebäude.",
                "Starker Regen verursacht einen Erdrutsch.",
                "Eine (angebliche) Hexe wird für ein seltenes Wetterphänomen verantwortlich gemacht und soll gelyncht werden."
              ]

dorf_magie = [
            "Mitten im Dorf kreuzen sich Kraftlinien.",
            "In der Nähe des Dorfes gibt es ein Feentor.",
            "Das Dorf zieht Mindergeister an.",
            "In der Nähe des Dorfes wohnt eine Hexe, ein Druide, ein Geode, ein Schamane …",
            "Im Ort befindet sich ein Artefakt.",
            "An bestimmten Tagen ist das Wasser einer nahen Quelle heilkräftig"
             ]

dorf_verlassen = [
                "Es finden sich Spuren eines Oger- oder Orkangriffs, aber die Bewohner sind verschwunden.",
                "Das Dorf ist schon seit Jahrzehnten unbewohnt.",
                "Eine Seuche hat fast alle Einwohner dahingerafft, die anderen sind davongezogen.",
                "Es sieht so aus, als hätten die Bewohner gerade erst alles stehen und liegen lassen.",
                "Die Bewohner sind Gefesselte Seelen und spuken nachts, wobei sie nicht wissen, dass sie tot sind.",
                "Alle Dorfbewohner sind in einem heiligen Wald in der Nähe, um einen Götterdienst zu halten oder einen Feenpakt zu erneuern."
                 ]

dorf_eigenart = [
                "Alle Dorfbewohner scheinen stumm zu sein, nicht einmal die Säuglinge schreien.",
                "Die Bewohner sind allesamt wahnsinnig."
                "Die Bewohner verehren eine finstere Gottheit und wollen ihr die Helden opfern.",
                "Ein Drache fordert ein Menschenopfer. Eigentlich soll es ein Jüngling aus dem Dorf sein, aber einer der Helden ist ein willkommener Ersatz.",
                "In der Nähe des Dorfes gibt es den Eingang zu einer großen unterirdischen Grabanlage.",
                "Im Dorf wohnt eine Familie von Exoten (Elfen, Achaz, Goblins …)."
                ]

dorf_situation = [
                "Eine Übeltäterin soll gerade gehängt oder verstümmelt werden.",
                "Eine Gruppe Holzfäller kommt aus dem Wald zurück.",
                "Die Fallenstellerin kehrt nach mehrtägiger Unternehmung zurück.",
                "Ein Bote kommt mit einer wichtigen Nachricht in das Dorf.",
                "Flüchtlinge erreichen das Dorf.",
                "Die Dorfbewohner packen ihre Sachen, um das Dorf zu verlassen"
                 ]

dorf_zauberer = [
                "Im Dorf wohnt eine Hexe.",
                "Das Dorf steht in respektvollem Kontakt mit einem Haindruiden.",
                "Am Rand des Dorfes steht der Turm einer eigenbrötlerischen Magierin.",
                "Im Dorf gibt es erstaunlich viele Magiedilettanten, die dadurch über erstaunliche Fähigkeiten verfügen, die für sie aber ganz normal sind.",
                "Da ein Bewohner des Dorfes ein Koboldfreund ist, hat sich das Dorf mit einer Koboldfamilie samt Schelmenkind arrangiert und wird von ihr auch tatkräftig unterstützt.",
                "Eine Dorfbewohnerin ist ein Feenkind."
                ]

dorf_geweiht = [
                "Ein Praios-Geweihter hält Gericht.",
                "Eine Nandus-Geweihte predigt gegen Unterwürfigkeit und wird aus dem Dorf gejagt.",
                "Ein Peraine-Geweihter segnet die Felder.",
                "Eine Firun-Geweihte wettert gegen Wilderei.",
                "Ein Efferd-Geweihter segnet den Brunnen oder eine Quelle, was der Quellnymphe nicht behagt.",
                "Die Priesterin einer regionalen Gottheit versucht die Helden zu bekehren."
               ]

dorf_liste = [
              dorf_fest,
              dorf_trauer,
              dorf_rast,
              dorf_probleme,
              dorf_religion,
              dorf_angriff,
              dorf_plagen,
              dorf_glaube,
              dorf_herrschaft,
              dorf_nacht,
              dorf_bdorfbewohner,
              dorf_bbauwerke,
              dorf_interak,
              dorf_wetter,
              dorf_magie,
              dorf_verlassen,
              dorf_eigenart,
              dorf_situation,
              dorf_zauberer,
              dorf_geweiht
              ]