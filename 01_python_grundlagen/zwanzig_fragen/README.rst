Zwanzig Fragen
===============

Übung 1: Führe das Programm aus
-------------------------------

Unten findest du den Code für das Spiel **zwanzig Fragen**.
In dem Spiel denkst du dir ein Tier aus.
Der Computer versucht, es mit nur Ja/Nein-Fragen zu erraten.

Um zu beginnen:

- lade den Code :download:`twenty_questions.py` herunter
- lade die Fragen in :download:`questions.json` herunter
- platziere beide Dateien im gleichen Ordner
- führe das Programm aus

Was passiert?

Hier ist der vollständige Code:

.. literalinclude:: twenty_questions.py

Übung 2: Lies den Code
-----------------------

Der einfachste Typ von Fehlern sind **Syntaxfehler**.
Ein Syntaxfehler bedeutet in der Regel, dass der Code vom Python-Interpreter nicht verstanden werden kann, sodass er ihn nicht ausführt.

Dieser Fehler ist am einfachsten zu beheben.
Eigentlich sollte dein Editor alle Syntaxfehler für dich finden.

Finde und behebe sie.

Übung 3: Fehlermeldungen lesen
------------------------------

Sobald du alle Syntaxfehler behoben hast, beginnt Python, den Code auszuführen.
Der nächste Fehler tritt auf, *während das Programm läuft*.
Diese Fehler werden als **Ausnahmen zur Laufzeit** bezeichnet.
Das Programm wird beendet und du siehst eine Fehlermeldung – so weißt du, dass ein Fehler aufgetreten ist.

Was kannst du über einen Fehler lernen, indem du die Fehlermeldung liest?
Versuche, die Fehler so gut wie möglich zu beheben.

.. hint::

   Eine gute Praxis beim Debuggen von Python-Code ist, Fehlermeldungen *von unten nach oben* zu lesen.

Übung 4: Diagnostische Ausgaben
-------------------------------

Viele Fehler erzeugen keine Fehlermeldung.
Für Python sieht alles gut aus.
Aber du stellst fest, dass das Programm nicht das tut, was es tun sollte.
Diese Kategorie, **semantische Fehler**, ist schwerer zu identifizieren,
weil du herausfinden musst, *dass* etwas schiefgeht und dann *was* genau schiefgeht.

Bei einem semantischen Fehler kannst du zusätzliche ``print``-Anweisungen in dein Programm einfügen,
damit du sehen kannst, was passiert.
Solche *diagnostischen Ausgaben* können so einfach sein wie:

.. code:: python3

   print("Punkt AAA")

oder du kannst den Inhalt einer Variablen anzeigen:

.. code:: python3

   print(finished)

Untersuche den nächsten Fehler mit einer zusätzlichen ``print``-Anweisung.
Entferne die ``print``-Anweisung, sobald der Fehler behoben ist.

Übung 5: Minimale Eingabe
-------------------------

Wenn dein Programm mit vielen Daten arbeitet, wird das Debuggen schwieriger.
Ein Problem bei dem Spiel ist, dass die JSON-Datei ``questions.json`` 
ein paar tausend Fragen enthält.

Verwende eine einfachere Datei.

Erstelle eine Datei ``mini_questions.json`` und verwende sie stattdessen, indem du den Dateinamen im Programm änderst.
Sie sollte die folgenden minimalistischen Daten enthalten:

::

    {
      "text": "ist es eine Python?",
      "yes": {
               "text": "es ist eine Python!"
               },
      "no": {
               "text": "es ist ein anderes Tier."
               }
    }

Wenn du das Spiel mit diesen Daten zum Laufen bekommst,
wechsle zurück zur größeren Datei.

**Viel Glück!**

Reflexionsfragen
----------------

* Welche Arten von Programmierfehlern kennst du?
* Welche Techniken zur Fehlersuche kennst du?
* Warum machen Programmierer Fehler?

.. seealso:: 

    - `Kristians Debugging Tutorial bei PyData 2017 <https://www.youtube.com/watch?v=04paHt9xG9U>`__
    - Daten von: `github.com/knkeniston/TwentyQuestions <https://github.com/knkeniston/TwentyQuestions/>`__

