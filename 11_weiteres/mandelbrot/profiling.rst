Mandelbrot
==========

Profiling von Python-Skripten
-----------------------------

Führe den Code in :download:`mandelbrot.py` aus und messe seine Ausführungszeit mit `cProfile`, dem Python Profiler:

.. code::

    python -m cProfile -s cumtime mandelbrot.py > profile.txt

Untersuche die Ausgabe und suche nach Engpässen.

Füge dann die folgende Zeile ein:

.. code:: python3

    z[index] = z[index] ** 2 + c[index]

Führe das Profiling erneut aus.

.. hint::

   cProfile funktioniert auch innerhalb eines Programms:

   .. code:: python3

       import cProfile
       cProfile.run("[x for x in range(1500)]")

Zeitmessung in Jupyter / IPython
--------------------------------

IPython (einschließlich Jupyter-Notebooks) verfügt über zwei magische Befehle zur Messung der Ausführungszeit.

.. code:: ipython3

    %time len(range(100000))

Vergleiche die Ausgabe mit

.. code:: ipython3

    %timeit
