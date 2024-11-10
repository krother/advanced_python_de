Finde das Drachenei
===================

|image0|

Weit, weit entfernt, in einer kaum zugänglichen Landschaft, liegt das mystische Drachenei versteckt. Wirst du das Ei finden und das Leben darin erwecken?

- das Drachenei befindet sich auf einer einsamen Lichtung
- um das Ei zu erwecken, brauchst du einen Zauberspruch
- der Zauberspruch ist nur einem Magier bekannt
- der Magier lebt in einem Turm hinter dem Wald
- im Wald lebt ein Bär, der niemanden vorbeilässt
- der Bär liebt jedoch Honig. Zum Glück gibt es einen Imker in der Nähe.

.. hint::

   Ich gebe zu, das ist nicht die größte Geschichte aller Zeiten. Wenn du eine bessere hast, programmiere sie!
   
Anforderungen
-------------

Schreibe ein Spiel, in dem du zwischen mehreren Räumen (Lichtung, Turm, Wald etc.) herumreisen kannst.

- die Welt besteht aus mindestens vier „Räumen“
- jeder Raum hat eine Beschreibung
- du gibst über die Tastatur ein, in welchen Raum du gehen möchtest
- wenn du das Ei findest, endet das Spiel mit einer Abschlussnachricht

Das Spiel ist komplett textbasiert.

Beispielausgabe
---------------

::

    *** Finde das Drachenei ***
    
    Du bist in deiner Heimatstadt, einem kleinen Handelsplatz an der Wüstengrenze.
    Es gibt Wege zu: Wüste, Wald
    
    Wohin möchtest du gehen? Wüste
    
    Du bist in der Wüste. Die Sonne brennt.
    Es gibt Wege zu: Heimat, Lichtung, Wald
    
    Wohin möchtest du gehen? Lichtung
    
    Auf einer verborgenen Lichtung entdeckst du das Drachenei.
    Deine Quest war erfolgreich!


----------------------------------------------

Schritt für Schritt
-------------------

Schritt 1: Erstelle einen Python-Datei
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Erstelle eine Python-Datei ``drachenei.py``
-  Öffne die Datei in einem Editor

Schritt 2: Die Grundstruktur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lass das Programm eine Begrüßungsnachricht ausgeben. Du könntest eine Ausgabe
mit mehreren Zeilen verwenden:

.. code:: python3

   print("""
   Finde das Drachenei
   ===================

   Deine Quest beginnt.
   """)

Am Ende gratuliert das Programm dem Spieler zum Erfolg:

.. code:: python3

   print("""
   Auf einer verborgenen Lichtung entdeckst du das Drachenei.

   Deine Quest war erfolgreich!
   """)

Während des Projekts wirst du mehr Code zwischen diesen beiden
Anweisungen einfügen.

**Führe das Programm aus und stelle sicher, dass es funktioniert.**

Schritt 3: Die Hauptschleife
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Das wichtigste Strukturelement der meisten Spiele ist die **Hauptschleife**.
In jeder Runde der Schleife kannst du einen Befehl eingeben. Das Spiel sollte enden, sobald du das endgültige Ziel erreichst.

Zu Beginn ist nicht bekannt, wie viele Anweisungen der Spieler eingeben wird.
Daher ist auch die Anzahl der Schleifendurchläufe unbekannt. In solchen Situationen ist eine **bedingte Schleife** mit ``while`` eine gute Wahl.

Zuerst musst du eine Variable definieren, die den aktuellen Standort enthält.
In Python kannst du den Namen des Raumes als String verwenden:

.. code:: python3

   room = "heimatstadt"

Sobald du den Raum *„Lichtung“* erreichst, endet das Spiel.
Du kannst das in der Bedingung der ``while``-Schleife überprüfen:

.. code:: python3

   while room != "lichtung":
       print(f"Du bist in {room}")
       room = input("Wohin möchtest du gehen? ")

**Führe das Programm aus und stelle sicher, dass du das Spiel beenden kannst.**


Schritt 4: Räume
~~~~~~~~~~~~~~~~

Dein Spiel hat noch keine Räume, daher ist es schwierig zu sagen, wo du dich befindest.

Schreibe interessante Beschreibungen der Räume und gib sie aus, indem du ``if``-Anweisungen wie die folgende zur Hauptschleife hinzufügst:

.. code:: python3

   if room == "heimatstadt":
       print("""
       Du bist in deiner Heimatstadt.
       Ein kleiner Handelsplatz an der Wüstengrenze.
       """)

Du kannst die ``print()``-Anweisung aus dem vorherigen Schritt durch die ``if``-Anweisung ersetzen.

**Führe das Programm aus und stelle sicher, dass es funktioniert.**


Schritt 5: Datenstruktur
~~~~~~~~~~~~~~~~~~~~~~~~

Jeden Raum mit einer separaten ``if``-Anweisung zu überprüfen, ist machbar, wenn du nur 4 Räume hast.
Aber stell dir vor, dein Spiel hätte 100 oder mehr Räume – das Programm würde ziemlich unübersichtlich werden.

Eine bessere Alternative ist es, die **Raumdaten zu strukturieren**.
Wir verwenden ein **Dictionary**, das die Beschreibungen aller Räume enthält:

.. code:: python3

   beschreibungen = {
       "heimatstadt": """Du bist in deiner Heimatstadt...""",
       "wüste": """...""",
   }

Definiere dieses Dictionary am Anfang des Programms.
Jetzt kannst du alle ``if``-Anweisungen durch eine einzige Abfrage im Dictionary ersetzen.
Der **Schlüssel** ist die Variable ``room``.

Füge diese Befehle zur ``while``-Schleife hinzu:

.. code:: python3

   print(beschreibungen[room])

und entferne die ``if``-Anweisungen aus Schritt 4.

**Führe das Programm aus und stelle sicher, dass es funktioniert.**

Schritt 6: Plausibilitätsprüfungen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Momentan überprüft das Programm nicht, ob der Raum, den du eingibst, tatsächlich existiert.
Wenn du einen falschen Raum eingibst (oder einen Tippfehler machst), beendet das Programm sich mit einer Fehlermeldung.

Lass uns die Eingabe überprüfen, um das zu verhindern.

Der folgende Code gleicht die Benutzereingabe mit den Schlüsseln des Dictionaries ``beschreibungen`` ab:

.. code:: python3

   ziel = input("Wohin möchtest du gehen? ")
   if ziel in beschreibungen:
       room = ziel
   else:
       print("Stopp! Dieser Ort existiert nicht.")

Finde heraus, an welcher Stelle im Programm diese Zeilen eingefügt werden müssen.

**Führe das Programm aus und stelle sicher, dass es funktioniert.**

Schritt 7: Pfade
~~~~~~~~~~~~~~~~

Bisher konntest du von einem Raum in jeden anderen teleportieren. Das macht das Spiel etwas langweilig.

-  Erstens ist nicht klar, in welche Räume du gehen kannst.
-  Zweitens könntest du einfach „Lichtung“ eingeben, und das Spiel endet sofort.

Das Spiel wäre viel interessanter, wenn nur einige Räume miteinander verbunden wären. Dafür brauchen wir ein zweites Dictionary, das die Verbindungen enthält. Jeder Eintrag zeigt von einem Ausgangsraum zu einem oder mehreren Zielräumen:

.. code:: python3

   wege = {
       "heimatstadt": ["imker", "wald"],
       "wald": ["heimatstadt", "wüste"],
       ...
   }

Du brauchst zwei Einträge, um Wege in beide Richtungen zu erstellen. Wenn du einen von ihnen weglässt, kannst du auch *Einbahnstraßen* schaffen.

Die möglichen Wege für den aktuellen Raum könnten mit folgender Zeile angezeigt werden:

.. code:: python3

   print(wege[room])

oder etwas schöner mit:

.. code:: python3

   print(", ".join(wege[room]))

Wenn du die Plausibilitätsprüfung erweitern möchtest, sodass nur die aktuellen Wege zugänglich sind, benötigst du die folgende Zeile:

.. code:: python3

   if ziel in wege[room]:
       ...

**Führe das Programm aus und stelle sicher, dass es funktioniert.**

Step 8: Puzzles
~~~~~~~~~~~~~~~

Ein spannendes Abenteuer sollte auch ein paar Rätsel enthalten. So könnte ein Rätsel aussehen:

::

   Wohin möchtest du gehen?
   Wald

   Es gibt einen BÄREN im Wald!!! Du rennst weg.

   Wohin möchtest du gehen?
   Imker

   Du kaufst einen Topf Honig beim Imker.

   Wohin möchtest du gehen?
   Wald

   Du lässt den Honigtopf für den Bären da und schleichst vorsichtig durch.


Wie implementiert man ein solches Rätsel?

Zuerst benötigst du eine **Statusvariable**, die du vor der Hauptschleife definierst, z.B.:

.. code:: python3

   honig = False

Zweitens musst du in der Hauptschleife überprüfen, ob sich der Status ändern sollte, und diesen dann entsprechend ändern, z.B.:

.. code:: python3

   if room == "imker" and not honig:
       print("Du kaufst einen Topf Honig beim Imker.")
       honig = True

Schließlich musst du die Statusvariable in der Hauptschleife überprüfen, um Aktionen zu erlauben oder zu verhindern:

.. code:: python3

    if ziel == "wald":
        if honig:
            print("Du lässt den Honigtopf für den Bären da und schleichst vorsichtig durch.")
            honig = False # du kannst den Honig nur einmal verwenden
         else: print("Es gibt einen BÄREN im Wald!!! Du rennst weg.")
            ziel = room # Spieler bleibt am selben Ort


.. |image0| image:: dragon_egg.png

