Decorators
==========

m Allgemeinen sind **Dekoratoren** Funktionen, die andere Funktionen erweitern. Genauer gesagt umhüllt ein Dekorator eine Funktion, um einem Funktionsaufruf zusätzliches Verhalten hinzuzufügen. In den folgenden Beispielen werden wir eine Python-Funktion dekorieren, die Fibonacci-Zahlen berechnet.

Verwendung eingebauter Dekoratoren
----------------------------------

Meistens verwendet man eingebaute Dekoratoren. Ein Beispiel ist `functools.lru_cache`, der das Ergebnis einer Funktion speichert, um später Zeit zu sparen. Dekorieren wir eine Funktion damit:

.. code:: python3

   from functools import lru_cache
   
   @lru_cache
   def fibonacci(n):
       """Recursively calculates fibonacci numbers"""
       if n < 2:
           return n
       return fibonacci(n-1) + fibonacci(n-2)

Versuche, eine rekursive Fibonacci-Zahl für `n=50` ohne den Dekorator zu berechnen. Es dauert ewig! Standardmäßig speichert `lru_cache` die letzten 128 Ergebnisse, sodass die Berechnung der rekursiven Fibonacci-Zahl darüber hinaus wieder langsamer wird.

Eingebaute Dekoratoren werden auch verwendet in:

-   Web-Frameworks wie **Flask** und **FastAPI**, um URLs Python-Funktionen zuzuordnen
-   dem **pytest**-Framework, um kompakten Testcode zu erstellen
-   Klassen mit `@property` und `@staticmethod` (im OOP-Abschnitt beschrieben)


------------------------------------------------------------------------

Eigene Dekoratoren schreiben
----------------------------

Wenn du eine Funktionalität hinzufügen möchtest, für die kein Dekorator existiert, z. B. das Drucken eines Zeitstempels bei jeder Addition, könntest du eine neue Funktion definieren:

.. code:: python3

   import time
   
   def fibonacci_with_timestamp(n):
       print(time.asctime())
       return fibonacci(n)


Wenn du die **Zeitstempelfunktion zu vielen Funktionen hinzufügen** möchtest, solltest du einen Dekorator verwenden:

.. code:: python3

   def print_timestamp(func):
   
       @functools.wraps(func)
       def wrapper(*args):
           print(time.asctime())  # done before addition
           result = func(*args)   # calls the addition function
           ...                    # actions after addition
           return result
   return wrapper
   
   
   @print_timestamp
   def fibonacci(n):
       """Recursively calculates fibonacci numbers"""
       if n < 2:
           return n
       return fibonacci(n-1) + fibonacci(n-2)
   
   # check docstring - would not work without @wraps
   print(help(addition))


Man könnte argumentieren, dass dies den Code nicht vereinfacht. Dekoratoren lohnen sich in größeren Programmen, wenn sie oft verwendet werden. Das Protokollieren von Funktionsaufrufen ist ein gutes Beispiel für die Verwendung eines Dekorators.

Der `@wraps`-Dekorator kopiert Dokumentationsstrings in die Dekoratorfunktion, sodass die dekorierte Funktion wie die Originalfunktion aussieht. Verwende dies beim Schreiben eigener Dekoratoren.

