#!/usr/bin/python3

#Schneider Gabriel / 23-08-2022
#Encounter Listen

stadt_main = ["Adelige",
              "Geweihte",
              "Zauberer",
              "Ordensleute",
              "Patrizier, Kaufleute und Krämer",
              "Handwerksmeister",
              "Ausrufer und Boten",
              "Bürokraten und Advokaten",
              "Handwerksgesellen",
              "Bewaffnete",
              "Barden und Gaukler",
              "Huren und Lustknaben",
              "Exoten",
              "Hilflose",
              "Bettler und Straßenkinder",
              "Schläger",
              "Verbrecher und Verbrechen",
              "Ungewöhnliche Funde",
              "Unfälle und Missgeschicke",
              "Übernatürliches"]

####################################################################


stadt_adelige =[
                "Ein prachtvoll gewandeter Adliger samt Gefolge spaziert durch die Stadt und ist auf dem Weg zu (s)einer Hochzeit oder einem Ball, oder er parliert laut über den Ankauf von Häusern oder Straßenzügen.",
                "Zwei Adlige haben sich den nächsten Platz für ein öffentliches Ehrenduell ausgesucht.",
                "Eine junge Frau in kostbarer Kleidung ist auf dem Weg zu einem Rendezvous, gleitet im Straßendreck aus und landet in demselben.",
                "Ein junger Mann in kostbarer Kleidung ist auf dem Weg zu einem Rendezvous, gleitet im Straßendreck aus und landet in demselben.",
                "Ein vornehmer Adelssprössling will in einem rauen Teil der Stadt 'Abenteuer erleben'.",
                "Rüpelhafte Adlige wollen Streit mit verfeindeten Patriziern des Stadtbürgertums provozieren.",
                "Ein Adliger möchte einem Konkurrenten einen Streich spielen und sucht Mithelfer"
                ]

stadt_geweihte =[
                "Eine Praios-Geweihten-Prozession zieht durch die Stadt.",
                "Ein Rondra-Geweihter bietet sich Streitenden als Schiedsrichter bei Duellen an.",
                "Eine Boron-Geweihte holt eine Verstorbene ab.",
                "Ein Phex-Geweihter im reich geschmückten Ornat wird von einigen Tölpeln überfallen.",
                "Eine Ingerimm-Geweihte predigt vor Zunftleuten die Erhabenheit des Handwerks.",
                "Ein Rahja-Geweihter bittet die Helden um Hilfe im Kampf gegen eine Zuhälterbande"
                ]

stadt_zauberer =[
                "Eine Weißmagierin belehrt die Helden über Gildengesetz und Zauberverbote.",
                "Ein Zauberer versucht sich durch Einsatz seiner Kräfte in der Öffentlichkeit Vorteile zu verschaffen (Einschüchtern von Passanten, Feilschen mit Händlern, schnellere Bedienung in der Taverne etc.).",
                "Zwei Zauberkundige tragen ein magisches Duell aus.",
                "Ein Zauberer (Hexe, Druide, Schelm, Magier) wird von Inquisition, Bannstrahlern, Stadtwache oder Pfeilen des Lichts gesucht oder abgeführt.",
                "Ein Zauberer sucht arkanen Nachwuchs und fragt die Helden nach geeigneten Kandidaten.",
                "Eine Scharlatanin führt magische Kunststücke vor."
                ]

stadt_orden = [
                "Ein Mönch vom Bund des wahren Glaubens predigt gegen Götzenkult und religiöse Gleichgültigkeit.",
                "Eine Badilakanerin sammelt für die Armen und predigt gegen Prostitution und Bordellbesuch.",
                "Zwei schweigsame Golgariten suchen nach Spuren von Untoten, die nachts umgehen.",
                "Die hochnäsige Dienerin eines Ordens fordert Ehrenbezeugungen.",
                "Ein Noionit und zwei Begleiter suchen einen entflohenen Irren.",
                "Eine gemäßigter Praios-Geweihte und ein fanatischer Bannstrahler tragen einen öffentlichen Disput aus."
              ]

stadt_händler = [
                "Ein Mitglied der Patrizierfamilien führt in einer auffallend schlichten Taverne Geschäftsgespräche.",
                "Ein Handelszug mit vielen Wagen verstopft eine Straße.",
                "Für die Feier einer Patrizierfamilie sollen die Helden (jenach Bekanntheit) als zusätzliche Wächter oder als prominente Ehrengäste angeworben werden.",
                "Ein unzufriedener Kunde droht einer Kauffrau mit Schlägen, wenn sie ihm nicht den Kaufpreis zurückerstattet.",
                "Ein penetranter Hausierer versucht, den Helden seine Waren aufzuschwatzen.",
                "Eine Krämerin belästigt Passanten mit Klagen über hohe Abgaben und schlechte Umsätze."
                ]

stadt_meister = [
                "Ein Meister kommandiert bei seiner Arbeit in der Werkstatt laut die Gesellinnen herum.",
                "Bei einer öffentlichen Zeremonie zur Aufnahme eines Lehrlings wird dieser nach altem Brauch von der Meisterin gedemütigt und erniedrigt.", 
                "Ein Waffenschmied bietet Rabatt, wenn die Helden für seine Waffen Werbung machen.",
                "Eine Meisterin mit ein paar Gesellen transportiert kostbare Waren oder Zunftgelder.",
                "Ein Zunftfest wird feierlich begangen. Fast alle Meister und Meisterinnen der Zunft sind zugegen, gerade wird die Zunftlade von Werkstatt zu Werkstatt getragen.",
                "Einige Handwerksmeister und -gesellen führen Waffenübungen für das städtische Aufgebot durch."
                ]

stadt_ausrufer = [
                "Eine offizielle Ausruferin trägt die neusten Nachrichten und Bekanntmachungen vor.",
                "Die Begleiter eines Ausrufers oder Boten verschaffen ihm rüde einen freien Weg.",
                "Ein Kind hat eine Nachricht für einen Helden, verlangt aber vor der Übergabe eine Bezahlung.",
                "Eine Botin mit dem Wappen einer Adligen sitzt in der Schänke und lässt sich volllaufen, statt ihre Pflichten zu erfüllen.",
                "Ein Hund apportiert dem tierliebsten Helden eine frisch getötete Brieftaube samt Nachricht.",
                "Ein verletzter Bote bittet die Helden um Weiterleitung seiner Botschaft.",
                 ]

stadt_advokat = [
                "Ein aufgeblasener Büttel will ein Exempel an den Helden statuieren und ein längst vergessenes Benimm-Gesetz durchsetzen.",
                "Eine Rechtsgelehrte will die Helden anwerben, um die Unschuld eines Mandanten zu beweisen.",
                "Eine städtische Amtsfrau fordert bei ihrer Inspektionen ungeniert Bestechungsgelder und könnte so das altbewährte System der Korruption gefährden.",
                "Ein Schreiber hastet mit zahllosen Schriftstücken über die Straße und verliert dabei einige Dokumente.",
                "Eine Bürokratin oder Rechtsgelehrte wird von Gaunern überfallen, die ihr Urkunden und Unterlagen stehlen sollen.",
                "Ein Rechtsgelehrter wird von einer ehemaligen Mandantin hart angegangen, er habe vor Gericht versagt und Unsummen Geld gekostet."
                ]

stadt_gesellen = [
                "Ein stadtfremder Geselle erkundigt sich nach zünftigen Meistern, bei denen er arbeiten kann.",
                "Gesellen und Gesellinnen feiern die Freisprechung des jüngsten aus ihrer Gruppe mit viel Bier und Schnaps.",
                "Gesellen verfolgen und verprügeln eine (echte oder angebliche) Schwarzarbeiterin oder Pfuscherin.",
                "Ein Trupp Gesellen und Gesellinnen hängt zechend beieinander und schimpft auf die ausbeuterischen Meister.",
                "Gesellen paradieren (oder patrouillieren) in 'ihrer' Nachbarschaft und schikanieren Bettler und andere 'Unruhestifter'.",
                "Gesellinnen sind unterwegs zu einer anderen Werkstatt (oder dem Zunfthaus), um einer feierlichen Zeremonie beizuwohnen."
                 ]

stadt_bewaffnet = [
                    "Spießbürger des Bürgerregimentes stolzieren umher und drängen alle Geringeren in den Sickergraben.",
                    "Der Werbetrupp einer Söldnereinheit hat in einer Taverne Quartier aufschlagen und wirbt Rekruten an.",
                    "Ein städtisches Waffenaufgebot kehrt siegreich aus Fehde oder Krieg zurück und wird in einer Parade gefeiert.",
                    "Die Stadtwache fordert einige Abenteurer auf, ihre übertriebene Bewaffnung abzulegen.",
                    "Stadtgardisten bei einer lästigen Routinekontrolle – bis sich die nervöse Gruppe vor den Helden als Bande gesuchter Verbrecher entpuppt.",
                    "Stadtwachen wollen nach Dienstende ihre schlechte Laune abreagieren."
                  ]

stadt_barden = [
                "Eine ärmlich gekleidete Gauklerin tritt auf. Die Vorstellung ist schlecht, weil die Ärmste vor Hunger kaum stehen kann.",
                "Ein vornehmer Sänger, begleitet vom eigenen Spielmann, trägt alte Weisen vor.",
                "Eine Bardin bittet die Helden um Erlebnisberichte, die sie für ihre Lieder verwenden will.",
                "Der vornehmste Held wird von einem Pantomimen nachgeäfft, sehr zum Vergnügen der meisten Umstehenden.",
                "Ein Barde wird von Geweihten aufgefordert, statt fröhlicher Tanzmusik nur noch fromme Lieder zu spielen.",
                "Zwischen einigen Barden und ein paar Handwerksgesellen kommt es zum regelrechten Sängerkrieg, als letztere mit ihren Zunftliedern alles niedergrölen wollen."
               ]

stadt_huren = [
                "Eine Dirnenmeisterin mit Begleitern, schwer parfümiert und leicht gekleidet, inspiziert Zunfthäuser.",
                "Dirnen steigen laut kichernd in die wappengeschmückte Kutsche eines Adligen.",
                "Liebesdiener oder Kuppler bieten aufdringlich ihre Dienst an.",
                "Eine gut gekleidete Frau verhandelt mit verschiedenen Huren und wählt diejenige aus, die sie ihrem Mann zum Tsafest verehren will.",
                "Ein junger Lustknabe wird von seiner (nicht zünftigen) Zuhälterin auf offener Straße geschlagen und misshandelt."
                "Aus einem Bordell wird ein Gast geworfen, der die geleisteten Dienste nicht bezahlen wollte."
              ]

stadt_exoten = [   
                "Ein Waldmensch wird von einem Gauklertrupp wie ein Tier im Käfig vorgeführt. Die Gaukler haben den naiven Waldmenschen einst unter einem Vorwand in den Käfig gelockt; die 'Medizin gegen seinen Fluch' ist ein Kraut, das ihn gefügig hält.",
                "Eine betrunkene Thorwalerin führt in einer Taverne Kraftkunststücke vor und stemmt Bänke mitsamt den Sitzenden in die Höhe, ohne die Betreffenden vorher um Erlaubnis zu bitten.",
                "Als ein Tölpel den aufreizenden Tanz einer Sharisad als Angebot missverstand, hat sie ihr Messer gebraucht. Nun fordern die Hinterbliebenen den Tod der 'mordenden Schlampe'.",
                "Ein Nicht-Zwölfgötter-Gläubiger hat sich in ein Viertel verirrt, wo seine Reden auf wenig Gegenliebe stoßen. Eine falsche Bemerkung des Hitzkopfs könnte einen schweren Zwischenfall entfesseln.",
                "Ein Elf tritt schon seit Wochen beim einfachen Volk als Sendbote des Elfenkönigs auf und verführt die Frauen (und manche Männer) der Nachbarschaft. Einigen Burschen missfällt das gewaltig, und Blutvergießen liegt in der Luft.",
                "Ein zwergischer Kaufmann wird von einigen Schlägern verfolgt, die ihn verprügeln und berauben wollen."
               ]

stadt_hilflose = [
                "Eine betrunkene Zecherin oder Rauschkrautgenießerin liegt am Straßenrand.",
                "Leibeigene Bauern haben sich in die große Stadt geflüchtet und suchen jemanden, der ihnen alles erklärt.",
                "Eine junge Frau bittet um Schutz vor Verfolgern.",
                "Kinder haben sich vom Elternhaus entfernt und finden nicht mehr zurück.",
                "Ein Reisender liegt in zerfetzter edler Kleidung blutend im Dreck.",
                "Schwer bepackte Flüchtlinge fragen die Helden, wer ihnen Almosen oder neues Land geben kann."
                 ]

stadt_bettler = [
                "Straßenkinder umringen die Helden und betasten staunend deren Ausrüstung. Wenig später fehlen einige Geldbeutel und Ausrüstungsteile.",
                "Eine kleine Göre erkennt einen berühmten Helden (oder glaubt das zumindest).",
                "Ein Bettler bittet die Helden um Hilfe bei der Rache an dem, der ihn zum Krüppel machte.",
                "Eine Bettlerin gibt sich als ehemalige Jugendfreundin oder Kampfgefährtin eines der Helden zu erkennen.",
                "Ein echter Invalide wird von einigen Unterweltlern bedrängt, die seinen Platz für einen Verkleideten aus ihren Reihen beanspruchen.",
                "Eine Bettlerin beschimpft oder verspottet die Helden."
                ]

stadt_schläger = [
                "Stadtbekannte Schläger wollen ihr Mütchen an den Helden kühlen.",
                "Söldner oder Beschützer ohne Heuer versuchen, einen blutigen Zwischenfall zwischen zwei städtischen Mächtegruppen anzuzetteln.",
                "Die Helden werden Zeuge, wie der Laden einer Kauffrau oder Handwerkerin kurz und klein geschlagen wird.",
                "Ein Raufbold hat sich in den Kopf gesetzt, ein Mitglied der Heldengruppe zu werden.",
                "Zwei Straßenbanden tragen eine Straßenschlacht aus, in die die Helden verwickelt werden",
                "Zwei Raufbolde tragen auf der Straße einen Faustkampf aus. Unter den Zuschauern nimmt jemand Wetten auf den Gewinner der Auseinandersetzung an, während mehrere Taschendiebinnen die günstige Gelegenheit nutzen."
                 ]

stadt_verbrecher = [
                    "Die Helden finden eine Leiche.",
                    "Die Helden ertappen eine Mörderin auf frischer Tat.",
                    "Jemand versucht, die Helden für ein Verbrechen anzuheuern.",
                    "Während er von seinen Gefährten getrennt ist, wird ein Held Ziel eines bewaffneten Überfalls.",
                    "Im Gedränge steckt eine Taschendiebin irrtümlich einem Helden statt ihrer Komplizin die Beute zu.",
                    "Einige Schlagetots kassieren gerade bei einem eingeschüchterten Wirt Schutzgeld."
                   ]

stadt_funde = [
            "Ein Geldbeutel, Schmuckstück, Siegelring",
            "Eine versiegelte oder verschlüsselte Botschaft",
            "Ein Tier läuft der Gruppe nach und weicht nicht von ihrer Seite.",
            "Zufällige Entdeckung einer gefangen gehaltenen Person.",
            "In einem Torweg liegen Kleidung, Waffen etc. eines Geweihten oder Adligen.",
            "In einem kleinen, verschrobenen Trödelladen kann man exotische Gegenstände erwerben. Bei späterer Suche ist es unmöglich, den Laden wiederzufinden."
              ]

stadt_unfall = [
                "Ein Geräusch versetzt ein Reitpferd oder die Zugtiere einer Kutsche in Panik.",
                "Bissige Straßenköter oder Wolfsratten fallen einen Passanten an.",
                "In einem Holzhaus bricht Feuer aus, das auf andere Gebäude übergreifen könnte.",
                "Eine Gerbergesellin stolpert und schüttet den Inhalt eines Nachttopfs über einen Passanten.",
                "Die für einen namhaften Offizier oder Recken gearbeitete Waffe zerbirst der erfahrenen Schmiedin beim Abschrecken.",
                "Der eigentlich sehr fähige Wirt im Stammlokal der Helden serviert plötzlich nur noch völlig ungenießbare oder verdorbene Mahlzeiten."
               ]

stadt_unnatur = [
                "Als ein vergessener Keller geöffnet wird, quellen Untote daraus hervor.",
                "Eine Kreatur aus der Wildnis wurde von einem Möchtegern-Helden verwundet. Nun ist sie zornig geworden und gefährdet die Menschen in der Stadt.",
                "Der Wasserspeier an einem alten Gebäude erwacht zu einem ebenso mordlustigen wie gerissenen und hinterlistigen Dasein.",
                "Ein Kobold ist in ein Haus eingezogen und macht den Bewohnern das Leben schwer.",
                "Ein Geist geht um und fordert erstaunlich materielle Opfer. Was steckt dahinter?",
                "Der Geist eines im Krieg Gefallenen sucht seine Familie oder sein Haus."
                ]

stadt_liste = [ stadt_adelige,
               stadt_geweihte,
               stadt_zauberer,
               stadt_orden,
               stadt_händler,
               stadt_meister,
               stadt_ausrufer,
               stadt_advokat,
               stadt_gesellen,
               stadt_bewaffnet,
               stadt_barden,
               stadt_huren,
               stadt_exoten,
               stadt_hilflose,
               stadt_bettler,
               stadt_schläger,
               stadt_verbrecher,
               stadt_funde,
               stadt_unfall,
               stadt_unnatur
               ]
               
