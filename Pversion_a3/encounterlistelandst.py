#!/usr/bin/python3

#Schneider Gabriel / 23-08-2022
#Encounter Listen

landst_main = ["Adelige",
              "Geweihte",
              "Zauberer",
              "Ordensleute",
              "Kaufleute und Händler",
              "Arbeiter",
              "Boten",
              "Bauer und Hirten",
              "Handwerker",
              "Bewaffnete",
              "Barden und Gaukler",
              "Gesetzeshüter",
              "Exoten",
              "Hilfsbedürftige",
              "Tiere",
              "Gelehrte",
              "verbrecher und Verbrechen",
              "Ungewöhnliches",
              "Ärgerliches",
              "Übernatürliches"]

####################################################################

landst_adel = [
            "Eine Reisekutsche mit vier weißen Pferden davor und mehreren bewaffneten Begleitern beansprucht die gesamte Straßenbreite.",
            "Eine Adlige verprügelt einen Bauern, der ihr nach ihrer Ansicht nicht schnell genug aus dem Weg gegangen ist.",
            "Ein Adliger hat offensichtlich Vorurteile gegen einen der Helden (z.B. einen Elfen, Zwergen, Novadi ...) und will ihn von seinem Land verscheuchen.",
            "Eine adlige Reisegruppe hat sich zur Rast niedergelassen und lädt die Helden ein, ihr Gesellschaft zu leisten.",
            "Eine Jagdgesellschaft kehrt mit reicher Beute nach Hause zurück.",
            "Eine Adlige erkennt einen der Helden und verlangt einen Beweis seiner Fähigkeiten."
              ]

landst_geweiht = [
                "Ein Wanderprediger will sich den Helden anschließen und sie dann in theologische Gespräche verwickeln.",
                "Eine freundliche Praios-Geweihte auf Quanionsqueste bittet die Helden um Geleitschutz durch gefährliches Gebiet.",
                "Ein Aves-Geweihter lädt die Helden zu einem bescheidenen Mahl ein und fragt sie nach ihren Erlebnissen.",
                "Eine Nandus-Geweihte bittet einen Helden um Hilfe bei der Entschlüsselung einer Inschrift nicht weit vom Weg entfernt.",
                "Ein Boron-Geweihter führt einen Begräbniszug zum etwas abseits gelegenen Friedhof.",
                "Eine Tsa-Geweihte lässt gutmütigen Spott über eine Respektsperson unter den Helden regnen."
                 ]

landst_zauberer = [
                "Eine Hexe bietet verletzten Helden Hilfe gegen geringes Entgelt.",
                "Ein Zauberer (Hexe, Druide, Schelm,Magier) wird von Inquisition, Bannstrahlern oder Pfeilen des Lichts gesucht oder abtransportiert.",
                "Eine magiekundige Hochstaplerin gibt sich als in Not geratene und hilfsbedürftige Adlige aus.",
                "Ein Schwarzmagier versucht, einen Helden zu entführen, um ihn zum Objekt eines magischen Experiments zu machen.",
                "Eine Goblin-Schamanin bittet die Helden um einen Gefallen und bietet ihnen im Gegenzug eine wertvolle erbeutete Waffe, die für Goblins absolut unhandlich ist.",
                "Eine reisende Magierin bittet um Geleitschutz."
                  ]

landst_orden = [
                "Ein Wanderprediger vom Bund des wahren Glaubens predigt bei einfachem Volk gegen Ungehorsam und mangelnde Götterfurcht.",
                "Eine Badilakanerin geleitet die Opfer eines Räuber-/Oger-/Trollüberfalls auf ihren Heimatort in die nächste Siedlung und bittet um Almosen.",
                "Zwei schweigsame Golgariten suchen nach Spuren von Untoten, die nachts umgehen.",
                "Die hochnäsige Dienerin eines Ordens fordert Ehrenbezeugungen.",
                "Ein Noionit und seine Begleiter suchen einen entflohenen Irren.",
                "Ein Trupp Amazonen fragt eine Heldin nach dem Weg."
               ]

landst_händler = [
                "Ein Kiepenkerl hat günstige Angebote, aber nichts Besonderes.",
                "Eine aufdringliche Krämerin mit Esels- oder Handkarren will unbedingt ins Geschäft kommen.",
                "Ein Norbarde (oder eine ganze Sippe) bietet alles an, was das Herz begehrt.",
                "Eine Quacksalberin will zweifelhafte Tinkturen verkaufen.",
                "Ein schwer beladener und gut bewachter Wagenzug kommt den Helden entgegen.",
                "Eine fahrende Händlerin bietet eine Schatzkarte / ein magisches Buch an."
                 ]

landst_arbeiter = [
                "Bauarbeiter reparieren Schäden an der Straße.",
                "Eine Brücke über einen Bach oder eine Felsspalte wird erneuert. Die Überquerung ist derzeit nur sehr vorsichtig möglich.",
                "An einer Wegkreuzung wird ein Schrein errichtet.",
                "Holzfällerinnen lassen von ihren Pferden schwere Baumstämme über die Straße ziehen.",
                "Um die Straße zu verbreitern, wird ein Stück aus einem Felsen herausgeschlagen.",
                "In der Nähe der Straße wird ein neuer Bauernhof erbaut."
                  ]

landst_boten = [
                "Ein berittener Bote prescht vorbei und drängt dabei einen Helden (fast) vom Weg.",
                "Die Helden finden ein herrenloses Pferd mit dem Brandzeichen eines Botendienstes. In der Satteltasche finden sich mehrere versiegelte Schreiben.",
                "Eine Botin überbringt einer Heldin eine Botschaft aus ihrer Heimat.",
                "Das Pferd eines Boten lahmt. Er bittet die Helden, ihm eines ihrer Pferde bis zur nächsten Wechselstation zu leihen, wo sie es wieder abholen können, wenn sie das lahmende Tier abgeben.",
                "Die Dienstzeit eines dämonischen Botenvogels endet in der Nähe der Helden, sodass er eine gesiegelte Nachricht fallen lässt, als er sich auflöst."
                "Die Helden finden die Reste einer von einem Raubvogel geschlagenen Brieftaube"
               ]

landst_bauer = [
                "Ein Bauer bringt Gemüse oder Obst zum Markt.",
                "Einer Magd, die Vieh zum Markt treiben will, ist ein Tier abhanden gekommen (zum Beispiel durch eine rücksichtslose Reiterin). Sie bittet die Helden, es wieder einzufangen.",
                "Eine Schafsherde blockiert die Straße.",
                "Eine Gruppe mit Dreschflegeln und Sensen bewaffneter Bauern und Bäuerinnen suchen nach einem Schelm / einem Ehebrecher / einem Hühnerdieb.",
                "Ein Waldschrat warnt die Helden davor, sich an seinen Bäumen zu vergreifen.",
                "Ein Knecht und eine Magd opfern nicht weit vom Weg entfernt lautstark Rahja."
               ]

landst_handwerker = [
                    "Ein Zwerg bietet für wenig Geld gute Waffenpflege an.",
                    "Eine fahrende Handwerksgesellin hat sich verlaufen und bittet um Hilfe."
                    "Ein Wagner ist einem verunglückten Ochsenkarren zu Hilfe geeilt und hat das zerbrochene Rad repariert. Um es auf die Achse zu stecken, braucht er kräftige Helfer, die den Wagen anheben.",
                    "Eine glück- und mittellose Handwerkerin versucht, etwas Essen aus den Taschen der Helden zu stehlen, weil sie seit einigen Tagen nichts zu beißen hatte.",
                    "Einige Maurer sind auf dem Weg zu einem Baron, der sich eine neue Burg errichten will.",
                    "Eine Schmiedin mit einer Wagenladung Roheisen hat Schwierigkeiten, eine Furt zu durchqueren"
                    ]

landst_bewaffnet = [
                    "Eine Ritterin mit ihrer Lanze (Knappin, Bannerträgerin, Gelehrte) fragt die Helden freundlich nach dem Woher und Wohin.",
                    "Ein Trupp Ordenskrieger reitet an den Helden vorbei und wirft ihnen misstrauische Blicke zu.",
                    "Eine zusammengewürfelte Abenteuergruppe rastet am Straßenrand und lädt die Helden ein, sich dazuzugesellen.",
                    "Ein kleiner Trupp Söldnerinnen wandert zu einer neuen Dienstherrin.",
                    "Eine Gruppe arbeitsloser und abgerissener Söldner wandert an den Helden entgegen. Wenn diese nicht sehr wehrhaft aussieht, 'bittet' der Anführer sie sehr eindringlich um ein angemessenes Almosen.",
                    "Eine Räuberbande lauert den Helden auf"
                   ]

landst_barden = [
                "Eine Bardin schließt sich den Helden an und bittet sie, ihr von ihren Heldentaten zu berichten.",
                "Ein Geschichtenerzähler / Haimamud fragt nach einer Mahlzeit und bietet im Gegenzug dafür eine Geschichte.",
                "Eine Gauklerin / Scharlatanin versucht, einen gutaussehenden Helden mit ihrer Kunst zu beeindrucken.",
                "Ein Narr / Schelm flüchtet vor erzürnten Einheimischen.",
                "Eine Theatergruppe zieht zur nächsten Ortschaft.",
                "Ein Tierbändiger, in dessen Wagen exotische Kreaturen ihr armseliges Dasein fristen, bittet die Helden, in der Umgebung nach einem exotischen Kraut zu suchen, das er für eine erkrankte Harpyie braucht."
                ]

landst_gesetz = [
                "Ein Richter ist unterwegs zu einem Dorfgericht.",
                "Eine Patrouille des örtlichen Adligen befragt die Helden, ob sie etwas zu einigen Viehdiebstählen sagen können.",
                "Eine Kopfgeldjägerin erkundigt sich nach einer flüchtigen Verbrecherin – und erkennt eventuell einen gesuchten Helden.",
                "Ein Ritter mit seinem Gefolge folgt der Spur einer Ork-, Goblin- oder Räuberbande und nimmt Hilfsangebote, gerne an.",
                "Eine Henkerin mit ihren Gehilfinnen wandert zu einer Hinrichtung.",
                "Ein Inquisitor mit Begleitung mustert die Helden und befragt sie, wenn sie sich auffällig verhalten."
                ]

landst_exoten = [
                "Ein in dieser Gegend nicht heimischer Exot (Waldmensch, Achaz, Halbork, Firnelf …) rastet am Wegrand.",
                "Eine Brückentrollin verlangt Zoll.",
                "Eine Goblinbande verlangt Wegzoll.",
                "Ein Elf überquert auf einer Regenbogenbrücke einen Fluss trockenen Fußes.",
                "Dorfbewohner verjagen eine Halborkin mit Steinwürfen.",
                "Ein Biestinger mustert die Helden neugierig."
                ]

landst_hilfslos = [
                "Am Wegrand steht ein grasendes, reiterloses Pferd.",
                "Den Helden kommt das Opfer eines Raubüberfalls entgegen.",
                "An der Kutsche eines Adligen ist ein Rad oder eine Achse gebrochen. Sie kann nur mit Hilfe kompetenter Helden repariert werden.",
                "Eine unbewaffnete Pilgergruppe bittet um Geleitschutz.",
                "Eine Bettlerin fragt nach Almosen.",
                "Die hungernden Kinder einer mittellosen TagelöhnerFamilie schauen den Helden beim Essen zu."
                  ]

landst_tiere = [
                "Ein niedlicher Wildschwein-Frischling läuft über die Straße. Die Bache ist bestimmt nicht weit.",
                "Ein aggressiver Stier sieht in den Helden potentielle Gegner und kommt schnaubend herangaloppiert.",
                "Ein Vogel mit verletztem Flügel hüpft über den Weg.",
                "Ein Raubvogel fühlt sich von der Anwesenheit der Helden gestört und fliegt Scheinangriffe.",
                "Eine erstaunlich große Katze oder Eule beobachtet die Helden von einem Baum herab.",
                "Ein Nachtwind greift einen magiebegabten Helden an."
               ]

landst_gelehrt = [
                "Eine reisende Medica bietet ihre Dienste gegen entsprechendes Entgelt.",
                "Ein tulamidischer Gelehrter, der kein Garethi spricht, hat sich auf der Suche nach einem geschichtsträchtigen Ort völlig verlaufen.",
                "Eine Kartographin vermisst Landschaftmarken und trägt sie in ein großes Buch ein.",
                "Ein offensichtlich geistig verwirrter Gelehrter faselt irgendwas von echsischen Intrigen.",
                "Eine Anatomin findet Interesse am Körperbau eines Helden und möchte ihn in allen (!) Einzelheiten vermessen.",
                "Ein dreckiger, ausgehungerter Mann in den zerlumpten Resten von Gelehrtenkleidung stolpert aus dem Wald und preist die Götter, endlich wieder Spuren der Zivilisation gefunden zu haben, nachdem ihm sein Führer abhanden gekommen ist."
                 ]

landst_verbrecher = [
                    "An einem Galgen baumeln die Reste einer Verbrecherin.",
                    "Ein Trupp Strafgefangener in Ketten bessert die Straße aus.",
                    "Eine Gruppe Bewaffneter führt eine Gefangene mit sich.",
                    "In einem schwer bewachten Käfigwagen sitzt ein gefangener Zauberer.",
                    "Einige Straßenräuberinnen wollen das Geld der Helden.",
                    "Die entkleidete Leiche eines Mordopfers liegt im Straßengraben und wird von einer Wolke aus Fliegen umsummt"
                    ]

landst_ungewohnt = [
                    "Seit dem letzten Weiler hat sich ein Hund einem Helden angeschlossen und will nicht von seiner Seite weichen.",
                    "Bei einer Rast handelt sich ein Held Ungeziefer ein (Zecken, Flöhe, Wanzen …).",
                    "Rechts und links der Straße sind alle Pflanzen abgestorben.",
                    "Die Ranken einer Pflanze kriechen auf die Helden zu.",
                    "Eine blühende Wiese verströmt geradezu betäubend intensiven Duft.",
                    "Nach einem kurzen Regenschauer leuchtet ein prächtiger Tsabogen am Himmel."
                   ]

landst_ärgerlich = [
                    "Ein langsamer Ochsenkarren lässt sich an einer Engstelle nicht überholen.",
                    "Ein Pferd der Helden verliert ein Hufeisen.",
                    "Weil der Fährmann schwer erkrankt ist, kann der Fluss hier derzeit nicht überquert werden.",
                    "Einem Karren oder einer Kutsche bricht ein Rad.",
                    "Ein großer umgestürzter Baum blockiert die Straße.",
                    "Eine Rotte Wildschweine hat die Straße zerwühlt und sie unpassierbar gemacht."
                   ]

landst_unnatur = [
                "Ein Kobold hockt am Wegesrand und bedenkt grimmig schauende Reisende mit seinen Scherzen.",
                "In der Ferne zieht ein Drache seine Kreise.",
                "Eine Taschendrachin besteht auf ein sofortiges philosophisches Gespräch mit einem gelehrten Helden.",
                "Ein Ikanaria-Schmetterling tanzt über den Weg.",
                "Ein hungriger Oger bricht aus dem Unterholz.",
                "Ein Irrlicht tanzt in der Ferne über einem Sumpfloch."
                 ]

landst_liste = [
                landst_adel,
                landst_geweiht,
                landst_zauberer,
                landst_orden,
                landst_händler,
                landst_arbeiter,
                landst_boten,
                landst_bauer,
                landst_handwerker,
                landst_bewaffnet,
                landst_barden,
                landst_gesetz,
                landst_exoten,
                landst_hilfslos,
                landst_tiere,
                landst_gelehrt,
                landst_verbrecher,
                landst_ungewohnt,
                landst_ärgerlich,
                landst_unnatur
                ]