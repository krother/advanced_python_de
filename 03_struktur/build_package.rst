
Baue ein Python-Paket
=====================

In dieser Übung verwenden wir `uv <https://docs.astral.sh/uv/>`__ um ein Python-Programm zu paketieren.
Du kannst das Programm aus dem vorigen Kapitel dafür verwenden.

Schritt 1: installation
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