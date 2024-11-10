"""
Beispiele für Typannotation (type hints)
ab Python 3.10

1. implementiere die Funktion
"""
from typing import Any, Literal

Frucht = Literal["Apfel", "Birne", "Cantaloupe"]

Obstkorb = set[Frucht]

Warenkorb = set[Any]

Obstpreise = dict[Frucht, float]

OBSTPREISE: Obstpreise = {
    "Apfel": 1.23,
    "Birne": 4.56,
    "Cantaloupe": 7.89,
}

def calc_total_price(waren: Warenkorb, preise: Obstpreise) -> float:
    ...


korb = {"Apfel", "Cantaloupe"}
print(calc_total_price(korb, OBSTPREISE))
