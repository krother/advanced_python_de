Generatoren
===========

Generatoren sind **lazy** Funktionen. Sie erzeugen Ergebnisse wie normale Python-Funktionen, aber nur dann, wenn sie gebraucht werden. Der Hauptzweck der Verwendung von Generatoren besteht darin, Speicher und Rechenzeit bei der Verarbeitung großer Datensätze zu sparen.

Ein Python-Generator wird durch das Schlüsselwort `yield` angezeigt. Eine `return`-Anweisung in einer Generatorfunktion beendet sie dennoch.

----

Ein minimalistisches Beispiel
-----------------------------

Der Aufruf der Funktion `powers()` initialisiert den Generator. Jedes Mal, wenn `next()` aufgerufen wird, wird ein Wert aus dem Generator abgerufen.

.. code:: python3::
   
   def powers():
       yield 1
       yield 2
       yield 4
       yield 8
       yield 16
   
   
   gen = powers()    
   print(next(gen))
   print(next(gen))
   print(next(gen))
   
----

Lazy evaluation
---------------

Beachten Sie, dass die Ergebnisse des Generators nicht vorab berechnet werden. Jeder Aufruf von `next()` führt den Code in der Generatorfunktion aus, bis die nächste `yield`-Anweisung erreicht wird.

Der folgende Code beweist das:

.. code:: python3

   def count():
       for i in range(10):
           print('checkpoint A')
           yield i
   
   gen = count()
   print('checkpoint B')
   print(next(gen))
   print(next(gen))


Der erste Aufruf des Generators tut zunächst nichts. Erst wenn `next()` den nächsten Wert anfordert, wird die Generatorfunktion bis zur `yield`-Anweisung ausgeführt. Dann pausiert sie bis zur nächsten `yield`-Anweisung und so weiter.

----

Werte verwenden
---------------

Um Werte aus einem Generator zu erhalten, kannst du eine `for`-Schleife oder Listenkonvertierung verwenden:

.. code:: python3

   for x in count():
       print(x, )

   print(list(count()))


----

Endlosschleifen
---------------

Generatoren können enlose Serien mit einer `while` erzeugen:

.. code:: python3

   def powers():
       """generates infinite powers of two"""
       n = 1
       while True:
           yield n
           n *= 2

Das Abrufen von Werten mit `next()` führt nicht zu einer Endlosschleife. Natürlich sollten Sie versuchen, diesen Generator weder in einer Schleife noch mit `list()` vollständig zu konsumieren.

----

Generator Expressions
---------------------

Generatoren lassen sich auch als Comprehension schreiben:

.. code:: python3

   squares = (x ** 2 for x in range(100))

   print(next(squares))


----

Iteratoren
----------

Generatoren liefern **iteratoren** zurück.
Viele Funktionen in Python verwenden Iteratoren (z.B. `range()`, `enumerate()` und
`zip()`).

Zu den Dingen, die Sie mit Iteratoren tun können, gehören:

-   Werte mit `next` anfordern.
-   Sie in einer `for`-Schleife verwenden.
-   Sie mit `list()` in Listen umwandeln.

Die Funktion `iter()` erstellt einen Generator aus jedem iterierbaren Objekt:

.. code:: python3

   gen = iter("Hello World")
   print(next(gen))  # -> 'H'
   print(next(gen))  # -> 'e'

