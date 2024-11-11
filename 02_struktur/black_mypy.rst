
Code aufräumen
==============

Übung 1: Typannotationen
------------------------

Füge Typannotationen zu den Argumenten und Rückgabewerten der Funktionen im Programm aus dem ersten Kapitel hinzu. Annotiere auch die wichtigsten Variablen mit Typen.

Führe den Code erneut aus und stelle sicher daß er funktioniert.

*Funktioniert das Progamm auch wenn du **falsche** Typen eingibst?*

Beispiel
++++++++

.. literalinclude:: type_annotations.py

Übung 2: Typen prüfen
---------------------

Installiere einen Type Checker für Python:

::
    
    python -m pip install mypy

Prüfe anschließend die Typen mit:

::

    mypy twenty_questions.py

Übung 3: Code Linter
--------------------

Säubere den Code mit:

::

    black twenty_questions.py
