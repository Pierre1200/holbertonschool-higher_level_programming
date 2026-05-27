#!/usr/bin/env python3
"""
Module pour la sérialisation et la désérialisation de données au format XML.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Sérialise un dictionnaire Python en format XML et le sauvegarde.
    Structure générée :
    <data>
        <cle1>valeur1</cle1>
        <cle2>valeur2</cle2>
    </data>
    """
    # 1. Création de la balise racine <data>
    root = ET.Element("data")

    # 2. Itération sur le dictionnaire pour ajouter des balises enfants
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # On force la conversion en chaîne pour le XML

    # 3. Création de l'arbre XML et écriture dans le fichier
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=False)


def deserialize_from_xml(filename):
    """
    Parse un fichier XML et reconstruit un dictionnaire Python 
    à partir de ses balises enfants.
    """
    try:
        # 1. Analyse (parsing) du fichier XML
        tree = ET.parse(filename)
        root = tree.getroot()

        # 2. Reconstruction du dictionnaire en parcourant chaque enfant
        deserialized_dict = {}
        for child in root:
            deserialized_dict[child.tag] = child.text

        return deserialized_dict

    except (FileNotFoundError, ET.ParseError):
        return None
