
# Datenrundreise

**Ziel: Daten in verschiedenen Formaten lesen und schreiben.**

### Übung 1: Den Baum abschreiten

Verwende ein kleines Python-Programm `traverse.py`, das die Datei `question.json` aus der Aufgabe **zwanzig Fragen** einliest und die Baumstruktur durchläuft.
Das Programm sollte eine Liste mit allen Fragen und Antworten erstellen.

**Sortiere die Zeilen in der Funktion `traverse()`.**

### Übung 2: Listen

Sammle die durchlaufenen Fragen und Antworten in zwei separate **Listen**:

    Fragen: [question_id, text, left_id, right_id]

    Antworten: [answer_id, text]

Du kannst fortlaufende Nummerierungen für Fragen und Antworten verwenden.

### Übung 3: Schreibe Tabellen

Verwende die Bibliothek `pandas`, um die Frage/Antwort-Daten in CSV-Dateien und Excel-Tabellen zu lesen und zu schreiben.
Der bereitgestellte Code-Schnipsel :download:`write_csv.py` bietet einen Ausgangspunkt.

Ersetze `csv` durch `excel`, um Tabellen zu lesen und zu schreiben.

### Übung 4: XML lesen

Schreibe das **pandas-DataFrame** mit Hilfe der Methode `to_xml()` in eine XML-Datei.

Verwende den Code-Schnipsel :download:`parse_xml.py`, um alle Fragen in den XML-Daten zu finden, die eines der folgenden Wörter enthalten:

    bird
    fly
    wing
    feather

### Übung 5: Schreibe JSON

Verwende das Modul `json`, um den ursprünglichen Baum in eine JSON-Datei zu schreiben.

Schreibe auch die Liste, die aus Übung 1 resultiert, in eine JSON-Datei. Vergleiche die Ergebnisse.

### Übung 6: SQL

Verwende das Code-Schnipsel :download:`read_write_sql.py`, um eine Tabelle in eine SQLite-Datenbank zu schreiben (außer der SQLAlchemy-Bibliothek ist keine Installation erforderlich).

Schreibe eine SQL-Abfrage, um Fragen/Antworten mit Schlüsselwörtern deiner Wahl zu finden.

### Reflexion

Erstelle eine Tabelle mit Vor- und Nachteilen der verschiedenen Formate.
