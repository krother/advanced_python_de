Römische Zahlen
===============

**🎯 Schreibe eine Funktion ``roman2arabic()``, die römische in arabische Zahlen überführt.**

Übung 1: Ein Test
-----------------

Beginne mit einem Test in einer Datei `test_roman.py`:

.. code:: python3

   def test_roman(self):
       assert roman2arabic("I") == 1

Führe den Test über die Kommandozeile aus mit:

::

   pytest

oder 

::

   python -m pytest

Übung 2: Code
-------------

Implementiere die Funktion in einem eigenen Modul.
Schreibe gerade genug Code, damit der Test erfolgreich ausgeführt wird.

Übung 3: Noch ein Test
----------------------

Füge einen Test hinzu. Führe ihn aus.
Schreibe etwas mehr Code.

Übung 4: Ein Grenzfall!
-----------------------

Als nächsten Test fange ungültige Eingaben ab:

.. code:: python3

   import pytest

   def test_invalid_input():
       with pytest.raises(IndexError):
           roman2arabic("77")

Auch dieser Test sollte erst fehlschlagen und dann erfolgreich werden.

Übung 5: Testparametrisierung
-----------------------------

Hier sind noch ein paar Beispiele:

.. code:: python3

   assert roman2arabic("XI") == 11
   assert roman2arabic("IX") == 9
   assert roman2arabic("CLI") == 151
   assert roman2arabic("XCIII") == 93
   assert roman2arabic("CCXCIV") == 294
   assert roman2arabic("MCM") == 1900
   assert roman2arabic("MI") == 1001

Naja, etwas redundant ist das ja schon.
Eleganter wird es mit folgendem Muster:

.. code:: python3

   @pytest.mark.parametrize("roman,arabic", [("I", 1), ("II", 2)])
   def test_many_romans(roman,arabic):
       assert ... 

Wenn du diesen Test ausführst, achte auf die Anzahl ausgeführter Testfunktionen.

.. hint::

   - beachte höchstens Zahlen von 1-5000
   - welche Datenstruktur eignet sich, um die Zahlenwerte der Buchstaben nachzuschlagen?
