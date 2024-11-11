
Baue ein Python-Paket
=====================

In dieser Übung verwenden wir `uv <https://docs.astral.sh/uv/>`__ um ein Python-Programm zu paketieren.
Du kannst das Programm aus dem vorigen Kapitel dafür verwenden.

Schritt 1: Installation
-----------------------

Installiere uv mit:

::

    python -m pip install uv

oder

::

    curl -LsSf https://astral.sh/uv/install.sh | sh


Schritt 2: Umgebung anlegen
---------------------------

Führe folgende Befehle aus:

::

    uv python install 3.11
    uv init

Schritt 3: pyproject.toml
-------------------------

Die Datei `pyproject.toml` enthält alles wichtige zum Projekt.
Du kannst dich an folgender Vorlage orientieren:

.. literalinclude:: pyproject.toml

Schritt 4: Bibliotheken installieren
------------------------------------

Die dependencies aus dem `pyproject.toml` werden installiert mit:

::

    uv lock
    uv sync

Schritt 4: Code ausführen
-------------------------

Ausführbare Skripte sind ebenfalls konfiguriert.
Im Beispielprogramm wäre das:

::

    uv run space

Schritt 5: Paket ausliefern
---------------------------

Erstelle aus dem Quelltext das Distributionsformat:
::

    uv build

Alle Dateien im Paketverzeichnise werden automatisch in den build aufgenommen.
Sie finden sich im Verzeichnis ``dist/``

Schritt 6: Paket installieren
-----------------------------

Das neu erstellte Paket ist nun mit ``pip`` aus der Datei installierbar:

::

    pip install dist/pandas_go_to_space-1.1.0-py3-none-any.whl

und

::

    python
    
    >>> import space_game
