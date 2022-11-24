#!/usr/bin/python3

#Schneider Gabriel / 23-08-2022
#Encounter Listen

wald_main = ["Adelige",
             "Geweihte",
             "Zauberer",
             "Ordensleute",
             "Händler",
             "Arbeiter",
             "Boten",
             "Gesetzeshüter",
             "Handwerker",
             "Bewaffnete",
             "Barden und Gaukler",
             "Pflanzen",
             "Exoten",
             "Hilfsbedürftige",
             "Tiere",
             "Gelehrte",
             "Verbrecher und Verbrechen",
             "Ungewöhnliches",
             "Unfälle und Missgeschicke",
             "Übernatürliches"
               ]

####################################################################

wald_adel =[
            "Eine Jagdgesellschaft bricht durchs Unterholz.",
            "Eine Gruppe Adliger mit Gefolge hat an einer Lichtung Zelte aufgebaut und genießt das Leben.",
            "Eine arrogante Ritterin befragt die Helden nach dem Woher und Wohin.",
            "Der Sprössling eines Adligen trifft sich heimlich mit einer Magd.",
            "Im verlassene Lager eines fahrenden Ritters finden die Helden Spuren eines Kampfes.",
            "Ein junge ritterliche Adlige ist auf der Suche nach einem Fabelwesen, um das Herz ihres Angebeteten zu erobern."
            ]

wald_geweiht =[
              "Ein Firun-Geweihter begegnet den Helden, ist aber an keiner Unterhaltung interessiert.",
              "Eine Tsa-Geweihte versucht den Helden ihren abendlichen Braten schlecht zu reden.",
              "Ein Peraine-Geweihter ist auf der Suche nach seltenen Kräutern und bittet die Helden um Hilfe.",
              "Eine Hesinde-Geweihte bittet die Helden um Hilfe bei der Entschlüsselung eines Runensteins.",
              "Ein Hesinde-Geweihter ist auf der Suche nach bisher unbekannten Pflanzen oder Tieren.",
              "Ein Trupp Boronis geht Hinweisen auf Untote nach und fragt die Helden nach Auffälligkeiten"
              ]

wald_zauber =[
            "Ein Druide will die Helden von seinem Gebiet verjagen.",
            "Die Helden finden einen verlassenen, aber auf magische Weise gesicherten Magierturm.",
            "Eine einsam lebende Hexe bietet den Helden eine Unterkunft für die Nacht an.",
            "Die Helden entdecken ein verlassenes Elfendorf.",
            "Die Helden geraten mitten in ein Hexenfest.",
            "Ein Geode möchte sich der Truppe für eine Weile anschließen, um etwas über Menschen zu lernen."
            ]

wald_orden =[
            "Einige Draconiterinnen suchen nach einem verschollenen Artefakt.",
            "Ein reisender Therbûnit bietet seine Hilfe an.",
            "Eine einsame und weltfremde Ardaritin hütet einen verlassenen Rondra-Tempel am Ort einer längst vergangenen Schlacht.",
            "Ein gefallener Golgarit sucht als Einsiedler in Meditation den Weg zurück zu seinem Gott.",
            "Eine Ingerimm-Geweihte hat sich in der Nähe eines (erloschenen) Vulkans einen kleinen Schmiedetempel gebaut.",
            "Mitten in der Einsamkeit steht das Kloster eines völlig unbekannten und recht eigenartigen Ordens"
            ]

wald_handel =[
            "Ein wortkarger Fallensteller oder Jäger kann frische Jagdbeute verkaufen.",
            "Eine Kräutersammlerin bietet frische Heilkräuter an.",
            "Ein Händler wollte mit seinem Karren eine Abkürzung nehmen und benötigt nun Hilfe, um weiterzukommen.",
            "Eine Zibilja ist auf der Suche nach einem gestohlenen Familienerbstück und überredet die Helden, ihr etwas Essen zu überlassen. Im Gegenzug bekommen sie von ihr etwas vollkommen Überflüssiges.",
            "Eine Gruppe Grolme bietet den Helden etwas an, was diese wirklich benötigen. Sie verlangen aber einen sehr hohen Preis dafür.",
            "Eine Koboldin findet das Konzept der Kaufens und Verkaufens sehr spannend und will auch mal."
            ]

wald_arbeit =[
              "Ein Holzfällertrupp fällt einige sehr alte Eichen, ohne zu ahnen, dass er sich dem Revier eines Waldschrats nähert.",
              "Einige Arbeiterinnen roden etwas Wald, weil sie hier ein neues Dorf gründen oder den Bau einer Burg vorbereiten sollen.",
              "Auf einer Hügelkuppe wird eine Festung errichtet. Man sieht bisher nicht viel mehr als die Fundamente.",
              "In einem Steinbruch wird edles Baugestein gebrochen.",
              "Bauleute brechen Steine aus den Mauern einer Burgruine, um sie für den Bau eines Dorfes in der Nähe zu verwenden.",
              "Eine Prospektorin sucht nach Anzeichen für Bodenschätze."
              ]

wald_bote =[
            "Die Helden treffen einen Boten, der einer Einsiedlerin irgendwo in dieser Gegend eine Nachricht überbringen soll.",
            "Ein junger Knecht ist auf dem Weg zur Baronin, da sein Heimatdorf Hilfe braucht.",
            "An einem verlassenen Lagerplatz finden die Helden die leergeräumte Tasche eines Botendienstes und einige weitere wertlose Beutestücke einer Räuberbande.",
            "In die Rinde eines Baumes ist eine kryptische Botschaft eingeritzt.",
            "Die Dienstzeit eines dämonischen Botenvogels endet in der Nähe der Helden, sodass er eine gesiegelte Nachricht fallen lässt, als er sich auflöst.",
            "Die Helden finden die Reste einer von einem Raubvogel geschlagenen Brieftaube."
            ]

wald_gesetz =[
              "Ein Dorfbüttel sucht nach einer entflohenen Leibeigenen.",
              "Ein paar bewaffnete Dorfbewohner folgen der Spur eines Räubers.",
              "Eine einheimische Ritterin mit seinem Knappen will in dieser Gegend für Ordnung sorgen.",
              "Eine Kopfgeldjägerin sucht nach einem Entflohenen.",
              "Ein Pfeil des Lichts forscht nach der Spur einer flüchtigen Zauberin.",
              "Ein Meckerdrache gibt sich als Herr dieses Waldes aus und will den Helden Vorschriften machen."
              ]

wald_handwerk =[
                "Eine Handwerkerin aus einem einsamen Dorf will auf den Markt in einer nahen Stadt.",
                "Ein Fallensteller überprüft gerade, ob er Beute gemacht hat.",
                "Eine Schreinerin sucht nach einem geeigneten Baum für einen großen Balken.",
                "Ein Steinmetz ist auf der Suche nach neuem Arbeitsmaterial.",
                "Die Helden treffen auf eine einsilbige, aber hilfsbereite Köhlerin.",
                "Ein Imker holt Honig aus einem Bienenstock."
                ]

wald_bewaffnet =[
                "Dorfbewohner sind von ihrer Herrin zu einem Gefecht gerufen worden.",
                "Die Helden entdecken den Zugang zu einem Räuberlager.",
                "Die Helden treffen einen übellaunigen Grenzreiter, der sie mürrisch darauf hinweist, dass das Gebiet seiner Herrin nicht ohne deren Erlaubnis betreten werden darf.",
                "Einige Soldaten machen Jagd auf Orks oder Goblins.",
                "Einige Goblins betrachten die Helden als zu gefährlich für einen Überfall und versuchen es mit einem Tauschgeschäft.",
                "Ein Trupp Orks betrachtet die Helden als potentielle Jagdbeute."
                ]
 
wald_barde =[
            "Einigen Schaustellern ist eines ihrer 'Haustiere' entflohen, nach dem sie nun suchen. Wenn die Helden Hilfe anbieten, nehmen sie gerne an.",
            "Eine Bardin hatte geglaubt, hier ein Dorf zu finden, in dem sie ihre Künste vorführen kann, sich dabei aber verirrt.",
            "Einige Gaukler wurden nach ihrem letzten Auftritt aus der Stadt gejagt und halten sich nun versteckt, bis niemand mehr nach ihnen sucht. Sie bitten die Helden, sie nicht zu verraten.",
            "Ein Barde oder Geschichtenerzähler sucht Inspiration in der Natur.",
            "Eine Scharlatanin übt einen für die Helden gefährlich wirkenden Illusionszauber (zum Beispiel das Bild eines Drachen oder umfallender Baums).",
            "Eine Nymphe sitzt an ihrer Quelle und singt bezaubernd schön."
            ]

wald_pflanze =[
              "Ein Held findet zufällig ein seltenes Heilkraut.",
              "Eine Heldin berührt unwissentlich eine Giftpflanze und bekommt juckenden oder blasenwerfenden Hautausschlag.",
              "Die Helden finden einen Baum mit reifen und leckeren Früchten.",
              "Ein Held läuft durch ein Gebüsch und ist danach mit Kletten bedeckt.",
              "Die Helden finden Pilze – essbar oder giftig.",
              "Die Helden finden die dämonisch pervertierte Form einer normalen Pflanze."
              ]

wald_exot =[
            "Die Helden begegnen einem Achaz (je nach Region eventuell in Kältestarre).",
            "Zwei goblinische Wildschweinreiter kreuzen den Weg der Helden.",
            "In einer einsamen Hütte lebt eine Frau mit ihrem halborkischen Kind.",
            "Die Helden treffen auf einen (entflohenen) Waldmenschen, der sich in der Wildnis durchschlägt.",
            "Die Helden begegnen einem verirrten Barbaren (Ferkina, Trollzacker, Gjalskerländer) fern seiner Heimat.",
            "Eine Firnelfe betrachtet die Helden misstrauisch, braucht aber ihre Hilfe, weil sie eine bestimmte Wegmarke nicht findet, von der ihre Vorfahren berichtet haben. Es ist fraglich, ob die Helden ihr helfen können."
            ]

wald_hilfe =[
            "Ein Kind ruft um Hilfe für einen Abgestürzten.",
            "Ein Kind ruft um Hilfe für einen Verletzten.",
            "Ein Aussätziger kämpft in der Abgeschiedenheit ums Überleben.",
            "Eine Holzfällerin ist unter einem Baum eingeklemmt.",
            "In einem Steinbruch gab es einen Felsrutsch, jemand ist verschüttet worden.",
            "Ein Wanderer wurde von einer Giftschlange gebissen und deliriert bereits.",
            "Eine Jägerin wurde von einem Eber angefallen und so schwer verletzt, dass sie es ohne Hilfe nicht zu ihrem Heimatdorf schafft."
            ]

wald_tier =[
            "Die Helden finden die Spur eines seltenen oder unbekannten Tiers.",
            "Die Helden werden von ausgehungerten Raubtieren angegriffen.",
            "Die Helden finden ein über mannsgroßes Spinnennetz.",
            "Ein Raubtier verhält sich ungewöhnlich zutraulich, möglicherweise ist es krank.",
            "Ein riesiger Schwarm Fledermäuse verdunkelt den Himmel."
            ]

wald_gelehrt =[
              "Eine Forscherin sucht nach alten Ruinen.",
              "Ein verwirrter Gelehrter erzählt etwas von einem riesigen Drachenhort.",
              "Eine weltfremde Gelehrte hat sich auf der Suche nach Paraphernalia verlaufen.",
              "Ein Gelehrter liegt am hellichten Tag unter einem Baum und schläft. Es handelt sich um einen Sternkundler, der glaubt, von hier aus nachts besondere Sternenkonstellationen beobachten zu können.",
              "Eine Anatomin ist auf der Suche nach menschenähnlichen Studienobjekten.",
              "Ein gelehrter Grabräuber vermutet in der Gegend alte Grabanlagen"
              ]

wald_verbrechen =[
                  "Eine Wilddiebin will ihre frische Beute nach Hause bringen.",
                  "Ein Schmuggler hat den Weg durch die Wildnis gewählt, weil er hier niemandem zu begegnen hoffte.",
                  "In einem Gebüsch liegt eine Leiche.",
                  "Eine Räuberbande überfällt gerade eine einsame Reisende.",
                  "Ein geflohener Leibeigener, der sich mit kleinen Diebstählen über Wasser hält, hat sich hier eine provisorische Hütte gebaut.",
                  "Anhänger eines verbotenen Glaubens haben sich im Verborgenen ein Dorf gebaut"
                  ]

wald_ungewöhn =[
                "Mehrere Hügel bilden die Silhouette eines liegenden Riesen.",
                "Ein verdorrter Baum hat noch einen Ast, an dem satte, grüne Blätter sprießen.",
                "Die Helden finden Tierspuren, die plötzlich in Menschenspuren übergehen.",
                "Es ist vollkommen still, kein Vogel singt, keine Insekten summen, kein Windrauschen ist zu hören.",
                "Ein beschnitzter Baumstamm erinnert an die Tabuzeichen der Waldmenschen.",
                "Ein zutrauliches Tier stellt sich als Biestinger heraus."
                ]

wald_missg =[
            "Teile des Proviants sind verdorben oder von Maden befallen.",
            "Ein Held wird von Ungeziefer befallen: Flöhe, Wanzen oder dergleichen.",
            "Eine Heldin verknackst sich den Fuß.",
            "Ein Hochwasser führender Bach zwingt die Helden zu einem Umweg.",
            "Ein plötzlicher Windstoß facht das Lagerfeuer an, es entsteht ein kleiner Brand.",
            "Einem Helden fällt ein morscher Ast (fast) auf den Kopf."
            ]

wald_unnatur =[
              "Ein Einhorn beobachtet die Helden aus der Ferne.",
              "Ein Waldschrat verwehrt den Helden den Weg durch seinen Wald.",
              "Die Helden finden einen verborgenen Steinkreis oder einen Hexentanzplatz.",
              "In der Ferne zieht ein Drache seine Kreise.",
              "Die Helden finden den Kultplatz eines fremdartigen Glaubens.",
              "Die Helden finden eine sprechende Alraune."
              ]

wald_liste = [
              wald_adel,
              wald_geweiht,
              wald_zauber,
              wald_orden,
              wald_handel,
              wald_arbeit,
              wald_bote,
              wald_gesetz,
              wald_handwerk,
              wald_bewaffnet,
              wald_barde,
              wald_pflanze,
              wald_exot,
              wald_hilfe,
              wald_tier,
              wald_gelehrt,
              wald_verbrechen,
              wald_ungewöhn,
              wald_missg,
              wald_unnatur
              ]