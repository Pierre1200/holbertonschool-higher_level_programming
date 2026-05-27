#!/usr/bin/env python3
"""
Module pour la sérialisation et la désérialisation d'objets personnalisés
avec le module pickle.
"""
import pickle


class CustomObject:
    """
    Classe personnalisée représentant un objet avec un nom, un âge
    et un statut d'étudiant.
    """

    def __init__(self, name: str, age: int, is_student: bool):
        """Initialise les attributs de CustomObject."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Affiche les attributs de l'objet selon le format spécifié."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Sérialise l'instance actuelle de l'objet et la sauvegarde
        dans le fichier spécifié en mode binaire.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (Exception, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Méthode de classe pour charger et désérialiser un objet CustomObject
        depuis un fichier binaire donné.
        Gère les exceptions pour les fichiers inexistants ou corrompus.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.PickleError, EOFError, Exception):
            return None
