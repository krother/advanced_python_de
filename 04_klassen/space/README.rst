Refaktorisieren
===============

**In dieser Übung refaktorisierst du Code mit Klassen.**

Dateien
~~~~~~~

- :download:`cli.py`
- :download:`game.py`
- :download:`location.py`
- :download:`mini_galaxy.json`
- :download:`galaxy_EN.json`

Übung 1: Pandas im Weltall
~~~~~~~~~~~~~~~~~~~~~~~~~~

Im Ordner für diese Sitzung findest du das Spiel **Pandas go to Space**.
Dies ist ein Python-Abenteuer, das ich für Programmierkurse entwickelt habe.

Starte das Spiel, indem du die textbasierte Benutzeroberfläche in ``cli.py`` ausführst mit

::

   python cli.py

Übung 2: Code Review
~~~~~~~~~~~~~~~~~~~~

Untersuche die drei Python-Dateien.
Je nach Erfahrung, schaue auf:

-  ``cli.py`` (einfach)
-  ``game.py`` (mittel)
-  ``location.py`` (fortgeschritten)

Du kannst auch die kleinere JSON-Datei inspizieren, um die Spieldaten anzusehen.

Markiere Abschnitte im Code, über die du mehr erfahren möchtest. Überlege außerdem, ob es Teile im Code gibt, die du problematisch oder schwer lesbar findest.

Übung 3: Traditionelle Python-Klassen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Untersuche die Klasse ``game.LoadCargoCommand``. Finde Folgendes heraus:

- den Klassennamen
- die Attribute und deren Typen
- die Methoden
- das self-Attribut
- ein Attribut, das innerhalb der Klasse aufgerufen wird
- ein Attribut oder eine Methode, die von außerhalb der Klasse aufgerufen wird

Übung 4: Klassen mit pydantic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Untersuche die Klasse ``location.Location``.
Vergleiche den Aufbau mit der vorigen Übung.

Übung 5: Erstelle eine Klasse
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Es wird Zeit sich von den globalen Variablen zu trennen. 
Erstelle eine neue Klasse ``Game`` in ``game.py`` mit drei Attributen:

-  location
-  cargo
-  crew

Erstelle eine globale Instanz von ``Game`` gleich nach der Definition:

::

   game = Game(...)

Ändere den Code,  so daß die Instanz verwendet wird, z.B. ``game.cargo``
anstelle von ``cargo``.

Führe das Programm aus und stelle sicher daß es funktioniert.

Übung 5: Erstelle eine Methode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Verschiebe die Funktion ``is_solved()`` in die ``Game``-Klasse:

-  rücke sie so ein, dass sie sich im Block der Klasse befindet
-  füge den Parameter ``self`` hinzu
-  ändere Verweise von ``game.`` zu ``self.``
-  ändere den Funktionsaufruf ``is_solved()`` zu ``game.is_solved()``

Stelle sicher, dass das Programm weiterhin funktioniert.

Übung 6: Objektkomposition
~~~~~~~~~~~~~~~~~~~~~~~~~~

Wo gibt es Komposition in der neuen Game-Klasse? Wäre es nicht einfacher, den Code aller Klassen zu einer zusammenzufassen?

Diskutiere, warum Komposition wichtig ist.

Übung 7: Vererbung und Polymorphismus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Erstelle eine Superklasse ``Command``:

::

   from abc import ABC, abstractmethod

   class Command(ABC):

       def __init__(self, name):
           self.name = name

       @abstractmethod
       def executed(self):
           pass

Verändere die übrigen Kommandos, so dass sie die neue Klasse verwenden.
Du kannst in den Subklassen geerbte Methoden verwenden:

::

   def __init__(self, name):
       super().__init__(self, name)
       ...

Übung 8: Statische Methoden
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Deklariere die Methode ``execute()`` als statisch, indem  du den
Dekorator ``staticmethod`` hinzufügst und den Parameter ``self`` wegläßt:

::

   @staticmethod
   def execute():
       ...

Bei welchen der anderen Methoden funktioniert das?
