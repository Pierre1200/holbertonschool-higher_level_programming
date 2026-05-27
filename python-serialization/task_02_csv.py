#!/usr/bin/env python3
"""
Module pour convertir des données d'un format CSV vers un format JSON.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Lit un fichier CSV donné en paramètre, convertit ses données
    en une liste de dictionnaires, et les écrit dans 'data.json'.

    Retourne True si la conversion réussit, False en cas d'erreur
    """
    try:
        # 1. Lecture du fichier CSV source
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            # DictReader lit automatiquement la première ligne
            csv_reader = csv.DictReader(csv_file)

            # Conv de l'itérateur de lignes en liste de dictionnaires
            data_list = [row for row in csv_reader]

        # 2. Sérialisation et écriture dans data.json
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file)

        return True

    except FileNotFoundError:
        # Gestion du cas où le fichier CSV d'entrée est introuvable
        return False
    except Exception:
        # Sécurité pour toute autre exception inattendue
        return False
