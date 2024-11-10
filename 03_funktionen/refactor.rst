
Refactoring
===========

**Ziel: Refaktorisiere den Code aus dem ersten Kapitel.**

Aufgabe 1: Eine Funktion extrahieren
------------------------------------
Refaktorisiere den Code so, dass er eine Funktion ``read_questions()`` enthält, die die Fragen aus einer Datei liest. Implementiere passende Funktionsparameter und Rückgabewerte. FügeTypannotationen für beide hinzu.

Führe den Code erneut aus und stelle sicher, dass er noch funktioniert.

Aufgabe 2: Eine weitere Funktion
--------------------------------

Wiederhole den Vorgang für einen anderen Teil des Codes und eine Funktion ``play()``.

Reflexionsfragen
~~~~~~~~~~~~~~~~

-  Wo befinden sich lokale Variablen im Code?
-  Gibt es globale Variablen?
-  Sollte man im Allgemeinen globale Variablen vermeiden?

Aufgabe 3: Hauptblock
---------------------

Erstelle einen ``__main__``-Block, der beide Funktionen aufruft.

Führe den Code erneut aus und stelle sicher, dass er noch funktioniert.

Aufgabe 4: Importierbares Modul
-------------------------------

Erstelle ein zusätzliches Modul ``questions.py`` und verschiebe die Funktionen dorthin.
Importiere die Funktionen korrekt.

Reflexionsfragen
~~~~~~~~~~~~~~~~

- Welche verschiedenen Importarten gibt es in Python?
- Woher importiert Python Module?
- Was ist PYTHONPATH?

Aufgabe 5: Ausnahmen abfangen
-----------------------------

Falls die Frage-Datei nicht gefunden wird, sollte das Programm mit einer Fehlermeldung
sanft beendet werden. Füge einen ``try.. except``-Block hinzu, der den ``FileNotFoundError`` abfängt.

Füge außerdem eine benutzerdefinierte Ausnahme ``TwentyQuestionError`` ein und löse diese aus,
wenn der Fragensatz leer ist.

Beispiel
--------

Folgenden Code kannst du als Ausgangspunkt verwenden:

.. literalinclude:: exception_example.py
