#!/usr/bin/env python3
"""Module serialisation"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Sérialise un dictionnaire Python et le sauvegarde dans un fichier JSON.
    Si le fichier existe déjà, il est automatiquement remplacé.
    """
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, f, indent=4)


def load_and_deserialize(filename):
    """
    Charge un JSON et le désérialise pour recréer le dictionnaire Python.
    Retourne le dictionnaire Python reconstruit.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
